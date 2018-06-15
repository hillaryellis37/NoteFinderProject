# import numpy as np
# import wave
# import struct
# import matplotlib.pyplot as plt
#
#
# frame_rate = 48000.0
# infile = "media/NylonChordAmaj.wav"
# num_samples = 48000
# wav_file = wave.open(infile, 'r')
# data = wav_file.readframes(num_samples)
# wav_file.close()
# amplitude = 16000
#
#
# data = struct.unpack('{n}h'.format(n=num_samples), data)
#
# data = np.array(data)
#
# data_fft = np.fft.fft(data)
#
#
# data_fft = [int(np.abs(s)/amplitude) for s in data_fft]
#
# print(data_fft[1000])
#
#
# #element with the highest amplitude:
#
# print("The frequency is {} Hz".format(np.argmax(data_fft)))
#
# #plot the results:
#
# plt.subplot(2, 1, 1)
#
# plt.plot(data[:300])
#
# plt.title("Original audio wave")
#
# plt.subplot(2, 1, 2)
#
# plt.plot(data_fft)
#
# plt.title("Frequencies found")
#
# plt.xlim(0, 1200)
#
# plt.show()

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
# rate, data = wav.read('media/Gmaj.wav')
rate, data = wav.read('media/Gmaj.wav')

fft_out = fft(data)


fft_out = [int(np.abs(s)/16000) for s in fft_out]


plt.plot(fft_out[:20000])
plt.xscale('log')
plt.show()


#need G,B,D
freq_max = np.argmax(fft_out)

print("The frequency is {} Hz".format(freq_max))


# filtering out freq:
#
filtered_freq = [f if index!= freq_max else 0 for index, f in enumerate(fft_out)]

freq_max = np.argmax(filtered_freq)

print(freq_max)