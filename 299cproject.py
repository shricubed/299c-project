from __future__ import division
import math
from pyaudio import PyAudio 

try:
    from itertools import izip
except ImportError:
    izip = zip
    xrange = range

def playNote(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), channels=1, rate=sample_rate, output=True)
                
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    for buf in izip(*[samples]*sample_rate):
        stream.write(bytes(bytearray(buf)))
    stream.write(b'\x80' * restframes)
    stream.stop_stream()
    stream.close()
    p.terminate()



