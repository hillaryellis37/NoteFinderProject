import argparse
import numpy as np
from NoteFinder.audio.FFT import FFT
from NoteFinder.audio.freq_to_note_converter import Note
from NoteFinder.plotting.bullseye_plot import Plot


wav_file_test = './NoteFinder/media/light_synth.wav'
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

    # create blank plot
    plot.start_plot()

    # create FFT object
    # fa_array= FFT(input_file=args.input_file)
    fa_array = FFT(input_file=wav_file_test)

    # create Note object
    fnote_converter = Note()

    def process_audio_stats(amp_array=None):

        if type(amp_array).__module__ == "builtins":

            # run FFT.run to extract loudest freq within the file
            loudest_freq, amplitude = fa_array.max_freq()
        else:
            loudest_freq, amplitude = fa_array.max_freq(amp_array=amp_array)

        # run Note.run to return note and freq range of note and freq ranges of all harmonics of the note:
        note, freq_range, freq_range_all, freq_harm = fnote_converter.run(loudest_freq)

        # returns array of amplitudes (12 total) for all harmonics of the note (inputs an array of freqs):
        note_amps = fa_array.amp_all_harm(freq_harm)

        # returns new array with previous highest amp set to masked:
        if type(amp_array).__module__ == "builtins":
            filtered_array = fa_array.filter_out_freq_range(freq_range_all)
        else:
            filtered_array = fa_array.filter_out_freq_range(freq_range_all, amp_array=amp_array)

        return note, note_amps, filtered_array

    ## run process_audio_stats x12 to get all 12 notes:
    note1, note_amps1, amp_array2 = process_audio_stats()
    note2, note_amps2, amp_array3 = process_audio_stats(amp_array=amp_array2)
    note3, note_amps3, amp_array4 = process_audio_stats(amp_array=amp_array3)
    note4, note_amps4, amp_array5 = process_audio_stats(amp_array=amp_array4)
    note5, note_amps5, amp_array6 = process_audio_stats(amp_array=amp_array5)
    note6, note_amps6, amp_array7 = process_audio_stats(amp_array=amp_array6)
    note7, note_amps7, amp_array8 = process_audio_stats(amp_array=amp_array7)
    note8, note_amps8, amp_array9 = process_audio_stats(amp_array=amp_array8)
    note9, note_amps9, amp_array10 = process_audio_stats(amp_array=amp_array9)
    note10, note_amps10, amp_array11 = process_audio_stats(amp_array=amp_array10)
    note11, note_amps11, amp_array12 = process_audio_stats(amp_array=amp_array11)
    note12, note_amps12, amp_array13 = process_audio_stats(amp_array=amp_array12)

    str_notes = note1[:-1] + " " + note2[:-1] + " " + note3[:-1] + " " + note4[:-1]
    print(notes)
    chord_notes = [note1[:-1], note2[:-1], note3[:-1], note4[:-1]]
    ## create 2d arrays all notes (in order of detected) and for amplitudes of all notes:

    all_notes = np.array([[note1], [note2], [note3], [note4], [note5], [note6], [note7], [note8], [note9], [note10], [note11], [note12]])

    all_amps = np.array([note_amps1, note_amps2, note_amps3, note_amps4, note_amps5, note_amps6, note_amps7, note_amps8, note_amps9, note_amps10, note_amps11, note_amps12])


    ## input 3 highest notes found to get chord:
    chord = fnote_converter.chord(str_notes)
    print(chord)

    plot.plot_amp(all_notes, all_amps, wav_file_test.split("/")[-1], chord_str=chord, note_list=chord_notes)

if __name__ == "__main__":
    main()