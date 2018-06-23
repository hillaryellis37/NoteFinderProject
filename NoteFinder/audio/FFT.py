
from pylab import*
from scipy.io import wavfile as wav
# from scipy.fftpack import fft
import numpy as np

wav_file_test = '../media/Gmaj.wav'

#boiler plate from: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1529536428.6186211109161376953125

class FFT:
    def __init__(self, input_file):

        self.input_file = input_file
        self.amplitude_array = []

        # parse wav file
        self.fs, self.dats = wav.read(self.input_file)
        # self.cols, self.rows = self.dats.shape
        #
        #
        # # check that wav file is valid for measurement
        # if self.dats.shape[1] == 2 or self.fs != 48000 or self.dats.dtype != np.int16:
        #     raise ValueError('chord finder only supports mono 48kHz, 16-bit wav files.')


        self.data = self.dats / (2.**15)
        self.data_length = len(self.data)
        self.data_fft = fft(self.data)

        self.nUniquePts = int(ceil((self.data_length+1)/2.0))

        self.fft_out = ((abs(self.data_fft[0:self.nUniquePts])) / float(self.data_length))**2

        if self.data_length % 2 > 0:
            self.fft_out[1:len(self.fft_out)] = self.fft_out[1:len(self.fft_out)] * 2
        else:
            self.fft_out[1:len(self.fft_out) -1] = self.fft_out[1:len(self.fft_out) - 1] * 2

        self.freqArray = (arange(0, self.nUniquePts, 1.0) * (self.fs / self.data_length)).astype(np.int64)

        plot(self.freqArray, 10*log10(self.fft_out), color='k')
        xlabel('Frequency (kHz)')
        ylabel('Power (dB)')
        show()

        for i in np.arange(0, 20001):

            self.amplitude_array.append(10*log10(self.fft_out)[np.searchsorted(self.freqArray, i)])




    #finds frequency with highest amplitude

    def max_freq(self):
        freq_max = np.argmax(self.amplitude_array)
        amplitude = self.amplitude_array[freq_max]

        print("The frequency is {} Hz".format(freq_max))
        print("The amplitude is {} Hz".format(amplitude))

        return freq_max, amplitude



    def filter_out_freq_range(self, freq_range):

        # for i in range(cols):
        #
        # # for j in range(len(fft_array)):
        #     fft_masked = np.array([0 if freq_range[i, 0] <= index <= freq_range[i, 1] else f for index, f in enumerate(fft_array)], dtype=float16)

        fft_filtered = np.array([-1000.0 if freq_range[0, 0] <= index <= freq_range[0, 1] or
                             freq_range[1, 0] <= index <= freq_range[1, 1] or
                             freq_range[2, 0] <= index <= freq_range[2, 1] or
                             freq_range[3, 0] <= index <= freq_range[3, 1] or
                             freq_range[4, 0] <= index <= freq_range[4, 1] or
                             freq_range[5, 0] <= index <= freq_range[5, 1] or
                             freq_range[6, 0] <= index <= freq_range[6, 1] or
                             freq_range[7, 0] <= index <= freq_range[7, 1] or
                             freq_range[8, 0] <= index <= freq_range[8, 1] or
                             freq_range[9, 0] <= index <= freq_range[9, 1]
                        else f for index, f in enumerate(self.amplitude_array)], dtype=float16)

        # fft_masked = np.ma.masked_equal(fft_filtered, 0.0)
        return fft_filtered

    def run(self):
        print('Running chord finder on input file: {}'.format(self.input_file))

        # max_freq = self.max_freq(self.amplitude_array)



# D = np.array([
#  [17.83154388,   18.89186265],
#  [35.66308775,   37.78372531],
#  [71.32617551,  75.56745061],
#  [142.65235101,  151.13490122],
#  [285.30470202,  302.26980244],
#  [570.60940405,  604.53960488],
#  [1141.21880809, 1209.07920976],
#  [2282.43761619, 2418.15841953],
#  [4564.87523237, 4836.31683905],
#  [9129.75046474, 9672.6336781]])
#
# G = np.array([
#  [23.80225543,    25.21761119],
#  [47.60451086,   50.43522238],
#  [95.20902171,   100.87044475],
#  [190.41804342,   201.74088951],
#  [380.83608684,   403.48177901],
#  [761.67217369,   806.96355802],
#  [1523.34434737,  1613.92711604],
#  [3046.68869474,  3227.85423208],
#  [6093.37738948,  6455.70846416],
#  [12186.75477897, 12911.41692832]])
#
# B = np.array([
#  [29.98896265,    31.77219916],
#  [59.9779253,     63.54439833],
#  [119.95585059,   127.08879666],
#  [239.91170119,   254.17759331],
#  [479.82340237,  508.35518662],
#  [959.64680475,  1016.71037325],
#  [1919.29360949,  2033.4207465],
#  [3838.58721898,  4066.84149299],
#  [7677.17443796,  8133.68298598],
#  [15354.34887593, 16267.36597196]])
#
# amp_array = wav_to_amp_array(wav_file_test)
#
# D_filtered = filter_out_freq_range(D, amp_array)
# D_filtered2 = max_freq(D_filtered)
#
# print(D_filtered[18])
# print(D_filtered[36])
# print(D_filtered[74])
# print(D_filtered[147])
# print(D_filtered[294])
# print(D_filtered[588])
# print(D_filtered[1175])
# print(D_filtered[2350])
# print(D_filtered[4699])
#
# G_filtered = filter_out_freq_range(G, D_filtered)
# G_filtered2 = max_freq(G_filtered)
#
# B_filtered = filter_out_freq_range(B, G_filtered)
# B_filtered2 = max_freq(B_filtered)



# Z = np.array([-117.25, -114.375, -106.5, -113.4375, -114.0625, -113.6875, -119.75, -109.625,
#  -106.25, -100.1875, -94.25, -94.4375, -96.6875, -100.4375, -98.6875, -94.875,
#  -89.75, -87.5625, -93.6875])
#
# fft_masked = np.ma.masked_equal(Z, -94.4375)
#
# print(np.argmax(fft_masked))
