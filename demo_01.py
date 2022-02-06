"""Demo."""
from time import sleep
from machine import I2C, I2S, Pin  # type: ignore
from sgtl5000 import CODEC

mclk = Pin(23)  # Master clock
bclk = Pin(21)  # Bit clock
dout = Pin(8)  # I2S data out from audio board to mcu
din = Pin(7)  # I2S data in from mcu to audio board
lrclk = Pin(20)  # word select left right clock
sda = Pin(18)  # I2C data
scl = Pin(19)  # I2C clock

i2c = I2C(0, freq=400000, scl=scl, sda=sda)

# audio_out = I2S(0,
#                 sck=bclk, ws=lrclk, sd=din,
#                 mode=I2S.TX,
#                 bits=16,
#                 format=I2S.STEREO,
#                 rate=44100,
#                 ibuf=20000)

# audio_in = I2S(1,
#                sck=bclk, ws=lrclk, sd=dout,
#                mode=I2S.RX,
#                bits=16,
#                format=I2S.STEREO,
#                rate=44100,
#                ibuf=20000)

sleep(1)
codec = CODEC(0x0A, i2c)

try:
    while True:

        sleep(.1)
except KeyboardInterrupt:
    print("\nCtrl-C pressed to exit.")
finally:
    pass
