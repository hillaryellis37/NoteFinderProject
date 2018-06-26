import argparse
import numpy as np
from NoteFinder.audio.FFT import FFT
from NoteFinder.audio.freq_to_note_converter import Note
from NoteFinder.plotting.bullseye_plot import Plot


wav_file_test = './NoteFinder/media/Gmaj.wav'
notes = ""

def main():

    """

    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Analyze spectral loudness of a 48 kHz, 16-bit stereo wav file.')
    parser.add_argument('--input_file', '-i', help='Path to input file. Must be .wav')

    args = parser.parse_args()

    # create Plot object:
    plot = Plot()

    # launch blank plot
    plot.start_plot()

    # create FFT object
    # fa_array= FFT(input_file=args.input_file)
    fa_array = FFT(input_file=wav_file_test)


    # run FFT.run to extract loudest freq within the file
    loudest_freq1, amplitude1 = fa_array.max_freq()


    # create Note object
    fnote_converter = Note()

    # run Note.run to return note and freq range of note and freq ranges of all harmonics of the note:
    note1, freq_range1, freq_range_all1, freq_harm1 = fnote_converter.run(loudest_freq1)

    note_amps1 = fa_array.amp_all_harm(freq_harm1)

    # plot.plot_amp(note1, note_amps1)

    #create a new array with the amplitude set to masked for all frequencies within range of the note:

    amp_array2 = fa_array.filter_out_freq_range(freq_range_all1)

    loudest_freq2, amplitude2 = fa_array.max_freq(amp_array=amp_array2)
    note2, freq_range2, freq_range_all2, freq_harm2 = fnote_converter.run(loudest_freq2)

    note_amps2 = fa_array.amp_all_harm(freq_harm2)

    amp_array3 = fa_array.filter_out_freq_range(freq_range_all2, amp_array=amp_array2)

    loudest_freq3, amplitude3 = fa_array.max_freq(amp_array=amp_array3)
    note3, freq_range3, freq_range_all3, freq_harm3 = fnote_converter.run(loudest_freq3)

    note_amps3 = fa_array.amp_all_harm(freq_harm3)

    amp_array4 = fa_array.filter_out_freq_range(freq_range_all3, amp_array=amp_array3)

    loudest_freq4, amplitude4 = fa_array.max_freq(amp_array=amp_array4)
    note4, freq_range4, freq_range_all4, freq_harm4 = fnote_converter.run(loudest_freq4)

    note_amps4 = fa_array.amp_all_harm(freq_harm4)

    notes = note1[:-1] + " " + note2[:-1] + " " + note3[:-1]


    #create 2d arrays all notes (in order of detected) and for amplitudes of all notes:

    all_notes = np.array([[note1], [note2], [note3], [note4]])

    all_amps = np.array([note_amps1, note_amps2, note_amps3, note_amps4])

    plot.plot_amp(all_notes, all_amps)




    chord = fnote_converter.chord(notes)
    print(chord)

if __name__ == "__main__":
    main()