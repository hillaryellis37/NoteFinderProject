
from pylab import*
from scipy.io import wavfile as wav
# from scipy.fftpack import fft
import numpy as np

wav_file_test = '../media/Gmaj.wav'

#boiler plate from: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1529536428.6186211109161376953125

class FFT:
    def __init__(self, input_file):

        self.input_file = input_file
        self.amplitude_array = np.array([-100.0])

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


        # plot(self.freqArray, 10*log10(self.fft_out), color='k')
        # xlabel('Frequency (kHz)')
        # ylabel('Power (dB)')
        # show()



        for i in np.arange(1, 20001):
            self.amplitude_array = np.append(self.amplitude_array, np.array([(10 * log10(self.fft_out)[np.searchsorted(self.freqArray, i)+3])]))

        self.amplitude_array = np.around(self.amplitude_array, decimals=5)

        # plot(np.arange(20001), self.amplitude_array, color='k')
        # xlabel('Frequency (kHz)')
        # ylabel('Power (dB)')
        # show()

    #finds frequency with highest amplitude

    def max_freq(self, amp_array=None):

        if type(amp_array).__module__ == "builtins":
            amp_array = self.amplitude_array


        freq_max = np.argmax(amp_array)
        amplitude = amp_array[freq_max]

        print("The frequency is {} Hz".format(freq_max))
        print("The amplitude is {} Hz".format(amplitude))

        return freq_max, amplitude



    def filter_out_freq_range(self, freq_range, amp_array=None):
        if type(amp_array).__module__ == "builtins":
            amp_array = self.amplitude_array

        note_amp_list=[]


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
                        else f for index, f in enumerate(amp_array)])

        # fft_masked = np.ma.masked_equal(fft_filtered, 0.0)
        return fft_filtered

    def amp_all_harm(self, note):
        harm_amps = []

        for i in range(len(note)):

            amp = self.amplitude_array[note[i]]
            harm_amps.append(amp)

        return harm_amps

    def run(self):
        print('Running chord finder on input file: {}'.format(self.input_file))

        # max_freq = self.max_freq(self.amplitude_array)




