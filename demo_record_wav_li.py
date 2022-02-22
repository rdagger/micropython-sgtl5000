"""Demo record WAV from line in."""
import os
from machine import I2C, I2S, Pin, SPI  # type: ignore
# from machine import SDCard  # Teensy 4.1 Built-in SD Card
from sdcard import SDCard  # Teensy 4.0 Audio adapter SD Card
from sgtl5000 import CODEC

spisd = SPI(0, baudrate=40000000)

""" SD Card baudrate should be set on SD Card class (Teensy 4.0 only):
Class 10 = 10 MHz
Class 6  =  6 MHz
Class 4  =  4 MHz
Class 2  =  2 MHz
Probably need a minimum of Class 6 depending on recording setttings"""
sd = SDCard(spisd, Pin(10), baudrate=10000000)  # Teensy 4.0 Audio SD Card
# sd = SDCard(1)  # Teensy 4.1: sck=45, mosi=43, miso=42, cs=44
os.mount(sd, "/sd")

# ======= I2S CONFIGURATION =======
SCK_PIN = 21
WS_PIN = 20
SD_PIN = 8
MCK_PIN = 23
I2S_ID = 1
BUFFER_LENGTH_IN_BYTES = 100000

# ======= AUDIO CONFIGURATION =======
WAV_FILE = "linein.wav"
RECORD_TIME_IN_SECONDS = 10
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.STEREO
SAMPLE_RATE_IN_HZ = 44100

format_to_channels = {I2S.MONO: 1, I2S.STEREO: 2}
NUM_CHANNELS = format_to_channels[FORMAT]
WAV_SAMPLE_SIZE_IN_BYTES = WAV_SAMPLE_SIZE_IN_BITS // 8
RECORDING_SIZE_IN_BYTES = (
    RECORD_TIME_IN_SECONDS * SAMPLE_RATE_IN_HZ * WAV_SAMPLE_SIZE_IN_BYTES * NUM_CHANNELS
)


def create_wav_header(sampleRate, bitsPerSample, num_channels, num_samples):
    """Generate WAV file header."""
    datasize = num_samples * num_channels * bitsPerSample // 8
    o = bytes("RIFF", "ascii")  # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(
        4, "little"
    )  # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE", "ascii")  # (4byte) File type
    o += bytes("fmt ", "ascii")  # (4byte) Format Chunk Marker
    o += (16).to_bytes(4, "little")  # (4byte) Length of above format data
    o += (1).to_bytes(2, "little")  # (2byte) Format type (1 - PCM)
    o += (num_channels).to_bytes(2, "little")  # (2byte)
    o += (sampleRate).to_bytes(4, "little")  # (4byte)
    o += (sampleRate * num_channels * bitsPerSample // 8).to_bytes(4, "little")  # (4byte)
    o += (num_channels * bitsPerSample // 8).to_bytes(2, "little")  # (2byte)
    o += (bitsPerSample).to_bytes(2, "little")  # (2byte)
    o += bytes("data", "ascii")  # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4, "little")  # (4byte) Data size in bytes
    return o


wav = open("/sd/{}".format(WAV_FILE), "wb")

# create header for WAV file and write to SD card
wav_header = create_wav_header(
    SAMPLE_RATE_IN_HZ,
    WAV_SAMPLE_SIZE_IN_BITS,
    NUM_CHANNELS,
    SAMPLE_RATE_IN_HZ * RECORD_TIME_IN_SECONDS,
)
num_bytes_written = wav.write(wav_header)

audio_in = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mck=Pin(MCK_PIN),
    mode=I2S.RX,
    bits=WAV_SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

# configure the SGTL5000 codec
i2c = I2C(0, freq=400000)
codec = CODEC(0x0A, i2c)
codec.vag_ramp(slow=True)  # Minimize Pop
codec.mute_dac(True)
codec.headphone_select(codec.AUDIO_HEADPHONE_LINEIN)  # Line In to headphones
codec.input_select(codec.AUDIO_INPUT_LINEIN)  # Recording input to Line In
codec.linein_level(15, 15)  # Maximum Line In levels
codec.mute_headphone(False)  # Enable headphone monitoring while recording
codec.volume(0.8, 0.8)  # Set headphone volume

# allocate sample arrays
# memoryview used to reduce heap allocation in while loop
mic_samples = bytearray(10000)
mic_samples_mv = memoryview(mic_samples)

num_sample_bytes_written_to_wav = 0

print("Recording size: {} bytes".format(RECORDING_SIZE_IN_BYTES))
print("==========  START RECORDING ==========")

try:
    while num_sample_bytes_written_to_wav < RECORDING_SIZE_IN_BYTES:
        # read a block of samples from the SGTL5000 I2S output
        num_bytes_read_from_mic = audio_in.readinto(mic_samples_mv)
        if num_bytes_read_from_mic > 0:
            num_bytes_to_write = min(
                num_bytes_read_from_mic, RECORDING_SIZE_IN_BYTES - num_sample_bytes_written_to_wav
            )
            # write samples to WAV file
            num_bytes_written = wav.write(mic_samples_mv[:num_bytes_to_write])
            num_sample_bytes_written_to_wav += num_bytes_written

    print("==========  DONE RECORDING ==========")
except (KeyboardInterrupt, Exception) as e:
    print("caught exception {} {}".format(type(e).__name__, e))

# cleanup
wav.close()
os.umount("/sd")
# sd.deinit()  # Teensy 4.1 Built-in SD Card
spisd.deinit()  # Teensy 4.0 Audio adapter SD Card
codec.deinit()
audio_in.deinit()
print("Done")
