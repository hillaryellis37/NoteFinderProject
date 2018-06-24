import argparse
import numpy as np
from NoteFinder.audio.FFT import FFT
from NoteFinder.audio.freq_to_note_converter import Note


wav_file_test = './NoteFinder/media/Gmaj.wav'

def main():

    """
    spectral_loudness.main() is the main command line entry point to use the spectral_loudness package.
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Analyze spectral loudness of a 48 kHz, 16-bit stereo wav file.')
    parser.add_argument('--input_file', '-i', help='Path to input file. Must be .wav')

    args = parser.parse_args()

    # create FFT object
    # fa_array= FFT(input_file=args.input_file)
    fa_array = FFT(input_file=wav_file_test)


    # run FFT.run to extract loudest freq within the file
    loudest_freq1, amplitude1 = fa_array.max_freq()

    # create Note object
    fnote_converter = Note(input_freq=loudest_freq1)

    # run Note.run to return note and freq range of note and freq ranges of all harmonics of the note:
    note, freq_range, freq_range_all = fnote_converter.run()

    print(freq_range_all, freq_range_all.dtype)

    #create a new array with the amplitude set to masked for all frequencies within range of the note:
    amp_array2 = fa_array.filter_out_freq_range(freq_range_all)

    print(amp_array2.dtype)
    print(amp_array2[:25])
    loudest_freq2, amplitude2 = fa_array.max_freq(amp_array=amp_array2)

    #repeat process for x4 total notes:








if __name__ == "__main__":
    main()