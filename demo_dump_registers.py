"""Demo all SGTL5000 registers to console for debugging."""
import os
from machine import I2C, I2S, Pin  # type: ignore
from sgtl5000 import CODEC
from sgtl5000_dump import DUMP

# ======= I2S CONFIGURATION =======
SCK_PIN = 21
WS_PIN = 20
SD_PIN = 7
MCK_PIN = 23
I2S_ID = 1
BUFFER_LENGTH_IN_BYTES = 40000

# ======= AUDIO CONFIGURATION =======
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.STEREO
SAMPLE_RATE_IN_HZ = 32000

audio_out = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mck=Pin(MCK_PIN),
    mode=I2S.TX,
    bits=WAV_SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

i2c = I2C(0, freq=400000)
codec = CODEC(0x0A, i2c, sample_rate=32000)
dump = DUMP(codec)
dump.print_all()

codec.deinit()
audio_out.deinit()
print("Done")


