Project Summary:



P1: The goal of the Chord Finder is too determine the most prevalent notes within an audio sample to determine the chord and display the notes and all existing harmonics of the notes on a plotted chart. 



The algorithm: 



The sample will get scanned and mapped to array using FFT
The freq with the highest amplitude is found and converted to note
Freq_to_note function: Inputs a frequency, outputs a note (for example: 440 Hz > “A4”)
The note along with all harmonics of that note will get extracted (set amp to 0) from the array and form a new array 
Note_to_Freq range function: Inputs a note, outputs a frequency range for all frequencies considered as that note (for example: “A4” > 427 Hz - 452 Hz)
Note_to_all_harmonics function: Inputs a note, outputs all harmonics within 20Hz - 20kHz by accessing the Note to Freq range function
The new array will get scanned again for the freq with the highest amp and again get extracted.
This above process will repeat until 4 notes are extracted from the sample. As long as each note has an amplitude enough to consider it signifiant: (In the case where a 1k sine tone sample will only show 1 note, for example)
Plotted data: The plotted chart will display a pie chart showing the top 4 notes found in the sample and determine the chord. Each note will be separated in 8 equal parts (splitting each note into 8 harmonics) and display a luminosity based on the amplitude of the harmonic.


Packages Used:

math (log2, pow)
numpy
wave
struct
spipy.io.wavefile
scipy.fftpack.fft
matplotlib.pyplot
music21

To Run Notefinder:

python note_finder.py -i'/path/to/file.wav'


