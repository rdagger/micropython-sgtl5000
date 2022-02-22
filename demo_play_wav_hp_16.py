"""Demo play WAV from SD to headphones using 16K sample rate."""
import os
from machine import I2C, I2S, Pin, PWM, SPI  # type: ignore
# from machine import SDCard  # Teensy 4.1 Built-in SD Card
from sdcard import SDCard  # Teensy 4.0 Audio adapter SD Card
from sgtl5000 import CODEC

spisd = SPI(0)
sd = SDCard(spisd, Pin(10), baudrate=10000000)  # Teensy 4.0 Audio SD Card
# sd = SDCard(1)  # Teensy 4.1: sck=45, mosi=43, miso=42, cs=44
os.mount(sd, "/sd")

# ======= PWM Configuration =======
MCK_PIN = 23
mclk=PWM(MCK_PIN, 10000000)

# ======= I2S CONFIGURATION =======
SCK_PIN = 21
WS_PIN = 20
SD_PIN = 7
I2S_ID = 1
BUFFER_LENGTH_IN_BYTES = 40000

# ======= AUDIO CONFIGURATION =======
WAV_FILE = "wav_music-16k-16bits-stereo.wav"
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.STEREO
SAMPLE_RATE_IN_HZ = 16000

audio_out = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=WAV_SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

i2c = I2C(0, freq=400000)
codec = CODEC(0x0A, i2c, mclk_freq=10000000, mclk_mode=3, sample_rate=16000)
codec.mute_dac(False)
codec.dac_volume(0.9, 0.9)
codec.headphone_select(codec.AUDIO_HEADPHONE_DAC)
codec.mute_headphone(False)
codec.volume(0.7, 0.7)

wav = open("/sd/{}".format(WAV_FILE), "rb")
_ = wav.seek(44)  # advance to first byte of Data section in WAV file

# allocate sample array
# memoryview used to reduce heap allocation
wav_samples = bytearray(10000)
wav_samples_mv = memoryview(wav_samples)

# continuously read audio samples from the WAV file
# and write them to an I2S DAC
print("==========  START PLAYBACK ==========")
try:
    while True:
        num_read = wav.readinto(wav_samples_mv)
        # end of WAV file?
        if num_read == 0:
            # end-of-file, advance to first byte of Data section
            _ = wav.seek(44)
        else:
            _ = audio_out.write(wav_samples_mv[:num_read])
except (KeyboardInterrupt, Exception) as e:
    print("caught exception {} {}".format(type(e).__name__, e))

# cleanup
wav.close()
os.umount("/sd")
# sd.deinit()  # Teensy 4.1 Built-in SD Card
spisd.deinit()  # Teensy 4.0 Audio adapter SD Card
codec.deinit()
audio_out.deinit()
mclk.deinit()
print("Done")
