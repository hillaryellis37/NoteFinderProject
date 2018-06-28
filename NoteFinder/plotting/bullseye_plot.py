import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

data = np.array(range(12)) + 1

fig = plt.figure(figsize=(12, 10))


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
theta = np.linspace(0, 2 * np.pi, 768)
r = np.linspace(0.0, 1, 11)

class Plot:
    def __init__(self, data=data, fig=fig, notes=notes, theta=theta, r=r):

        self.data = data

        # Make a figure and axes with dimensions as desired.

        self.fig = fig
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar', facecolor="#E8E8E8")

        self.notes = notes
        self.theta = theta
        self.r = r

        # Set the colormap and norm to correspond to the data for which
        # the colorbar will be used.

        self.cmap = mpl.cm.inferno
        self.norm = mpl.colors.Normalize(vmin=1, vmax=12)


    def bullseye_plot(self, ax):

        for i in range(self.r.shape[0]):
            self.ax.plot(self.theta, np.repeat(self.r[i], self.theta.shape), '-k', linewidth=.45)

        for i in range(12):
            theta_i = i*30*np.pi/180

            self.ax.plot([theta_i, theta_i], [self.r[0], 1], '-k', linewidth=.45)


        ax.set_ylim([0, 1])

        ax.set_yticks(np.linspace(0, 1, 11))
        ax.set_yticklabels(range(10))
        ax.set_xticks(np.linspace(0, 12*60*np.pi/360, 13))
        ax.set_xticklabels(self.notes)



    def plot_amp(self, note_array, amp_array, sample_name, chord_str=None, note_list=None):

        if note_list is None:
            note_list = []

        segBold = [self.notes.index(note_list[i]) for i in range(len(note_list))]

        amp_array_1d = amp_array.flatten()

        amp_array_1d_2 = amp_array.flatten()
        amp_array_1d = (amp_array_1d*-1)**(amp_array_1d*-1/((amp_array_1d*-30)**2))

        normalized = (amp_array_1d - min(amp_array_1d)) / (max(amp_array_1d) - min(amp_array_1d))
        normalized2 = (amp_array_1d_2 - min(amp_array_1d_2)) / (max(amp_array_1d_2) - min(amp_array_1d_2))

        normalized = normalized.reshape(amp_array.shape)
        normalized2 = normalized2.reshape(amp_array.shape)

        for j in range(note_array.shape[0]):

            note_pos = self.notes.index(note_array[j,0][:-1])

            for i in range(10):

                rind = self.r[i:i + 2]
                rind = np.repeat(rind[:, np.newaxis], 64, axis=1).T
                theta0 = self.theta[note_pos * 64:note_pos * 64 + 64]
                theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)

                if normalized[j,i] >= .7:
                    z = np.ones((64, 2)) * (self.data[11], self.data[note_pos])
                elif normalized[j,i] >= .45:
                    z = np.ones((64, 2)) * (self.data[10], self.data[note_pos])
                elif normalized[j,i] >= .4:
                    z = np.ones((64, 2)) * (self.data[9], self.data[note_pos])
                elif normalized[j,i] >= .38:
                    z = np.ones((64, 2)) * (self.data[8], self.data[note_pos])
                elif normalized[j,i] >= .36:
                    z = np.ones((64, 2)) * (self.data[7], self.data[note_pos])
                elif normalized[j,i] >= .34:
                    z = np.ones((64, 2)) * (self.data[6], self.data[note_pos])
                elif normalized[j,i] >= .31:
                    z = np.ones((64, 2)) * (self.data[5], self.data[note_pos])
                elif normalized[j,i] >= .28:
                    z = np.ones((64, 2)) * (self.data[4], self.data[note_pos])
                elif normalized[j,i] >= .25:
                    z = np.ones((64, 2)) * (self.data[3],self.data[note_pos])
                elif normalized[j,i] >= .2:
                    z = np.ones((64, 2)) * (self.data[2], self.data[note_pos])
                elif normalized[j,i] >= .15:
                    z = np.ones((64, 2)) * (self.data[1], self.data[note_pos])
                elif normalized[j,i] >= .1:
                    z = np.ones((64, 2)) * (self.data[0], self.data[note_pos])
                else:
                    z = np.ones((64, 2)) * (self.data[0], self.data[note_pos])


                self.ax.pcolormesh(theta0, rind, z, cmap=self.cmap, norm=self.norm, alpha=normalized2[j,i])

                if note_pos in segBold:
                    for i in range(len(self.r)):

                        r0 = r[i:i+2]
                        r0 = np.repeat(r0[:, np.newaxis], 64, axis=1).T

                    for i in range(12):

                        theta0 = self.theta[i*64:i*64+64]
                        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)

                        # to outline the notes in chord:
                        if i in segBold:
                            self.ax.plot(theta0, r0, '-k', lw=4)
                            self.ax.plot(theta0[0], [self.r[0], self.r[10]], '-k', ls='--', lw=3)
                            self.ax.plot(theta0[-1], [self.r[0], self.r[10]], '-k', ls='--', lw=3)
        # plot settings:

        self.ax.plot('-k', ls='--', lw=3, label="chord found: " + chord_str)
        self.ax.plot('-k', ls='--', lw=3, label="Notes in chord: " + str(note_list))
        self.ax.set_title("Harmonics and Overtones found in: " + sample_name)
        axl = self.fig.add_axes([0.1, 0.1, 0.2, 0.05])

        self.ax.legend(bbox_to_anchor=(.7, 0, 0.5, 1))

        bounds = []

        cb = mpl.colorbar.ColorbarBase(axl, cmap=self.cmap, norm=self.norm, alpha=.5, ticks=bounds, orientation='horizontal')
        cb.set_label('Amplitude in dB')

        plt.show()


    def start_plot(self):


        self.bullseye_plot(self.ax)



