import wave
import struct
import math
import os
from scipy import fromstring, int16

file = os.path.exists("data")
print(file)

if file == False:
    os.mkdir("data")

def cut_wav(filename,time): 
    wavf = filename + '.wav'
    wr = wave.open(wavf, 'r')

    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    integer = math.floor(total_time)
    t = int(time)
    frames = int(ch * fr * t)
    num_cut = int(integer//t)

    data = wr.readframes(wr.getnframes())
    wr.close()
    X = fromstring(data, dtype=int16)

    for i in range(num_cut):
        print(i)
        outf = 'data/' + str(i) + '.wav' 
        start_cut = i*frames
        end_cut = i*frames + frames
        print(start_cut)
        print(end_cut)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        ww = wave.open(outf, 'w')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()

print("input filename >>")
f_name = input()
print("cut time >>")
cut_time = input()
cut_wav(f_name,cut_time)
