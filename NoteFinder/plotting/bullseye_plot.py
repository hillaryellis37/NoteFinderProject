import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import iqr

data = np.array(range(12)) + 1

fig = plt.figure(figsize=(6, 6))


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
theta = np.linspace(0, 2 * np.pi, 768)
r = np.linspace(0.0, 1, 11)

class Plot:
    def __init__(self, data=data, fig=fig, notes=notes, theta=theta, r=r):

        self.data = data

        # Make a figure and axes with dimensions as desired.

        self.fig = fig
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8],
                          projection='polar')

        self.notes = notes
        self.theta = theta
        self.r = r

        # Set the colormap and norm to correspond to the data for which
        # the colorbar will be used.
        self.cmap = mpl.cm.inferno
        self.norm = mpl.colors.Normalize(vmin=1, vmax=12)
        # self.color = "#4b0082"
        # self.cmap = None
        # self.norm = None
        # self.color = None


    def bullseye_plot(self, ax, data, segBold=None, cmap=None, norm=None):

        # if segBold is None:
        #     segBold = []
        #
        # linewidth = 2
        # data = np.array(data).ravel()

        # if cmap is None:
        #     cmap = self.cmap
        #
        # if norm is None:
        #     norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max())
        #     # norm = self.norm

        for i in range(self.r.shape[0]):
            ax.plot(self.theta, np.repeat(self.r[i], self.theta.shape), '-k', linewidth=1)

        for i in range(12):
            theta_i = i*30*np.pi/180

            ax.plot([theta_i, theta_i], [self.r[0], 1], '-k', linewidth=.5)


        # for i in range(len(self.r)):
        #
        #     r0 = r[i:i+2]
        #     r0 = np.repeat(r0[:, np.newaxis], 64, axis=1).T


            # for i in range(12):

                # theta0 = self.theta[i*64:i*64+64]
                # theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
                #
                # z = np.ones((64, 2))*data[i]
                #
                # ax.pcolormesh(theta0, r0, z, cmap=self.cmap, norm=self.norm, alpha=.5)
                #
                # if i+1 in segBold:
                #     ax.plot(theta0, r0, '-k', lw=linewidth+2)
                #     ax.plot(theta0[0], [self.r[2], self.r[3]], '-k', lw=linewidth+1)
                #     ax.plot(theta0[-1], [self.r[2], self.r[3]], '-k', lw=linewidth+1)

        ax.set_ylim([0, 1])

        ax.set_yticks(np.linspace(0, 1, 11))
        ax.set_yticklabels(range(10))
        ax.set_xticks(np.linspace(0, 12*60*np.pi/360, 13))
        ax.set_xticklabels(self.notes)



    def plot_amp(self, note_array, amp_array):
        # print(amp_array.shape)


        amp_array_1d = amp_array.flatten()

        amp_array_1d_2 = amp_array.flatten()
        amp_array_1d = (amp_array_1d*-1)**(1/amp_array_1d**2)



        # standardized  = (amp_array_1d - np.mean(amp_array_1d)) / (max(amp_array_1d) - min(amp_array_1d))
        # normalized2 = (standardized - min(standardized)) / (max(standardized) - min(standardized))
        normalized = (amp_array_1d - min(amp_array_1d)) / (max(amp_array_1d) - min(amp_array_1d))
        normalized2 = (amp_array_1d_2 - min(amp_array_1d_2)) / (max(amp_array_1d_2) - min(amp_array_1d_2))


        # print(amp_array_1d)
        normalized = normalized.reshape(amp_array.shape)
        normalized2 = normalized2.reshape(amp_array.shape)

        print(normalized[0])
        print(normalized2[0])

        for j in range(note_array.shape[0]):
            note_pos = self.notes.index(note_array[j,0][:-1])

            # normalized = (amp_array - ) / (max(amp_array) - min(amp_array))
            # z = np.ones((64, 2)) * (j,self.data[note_pos])


            for i in range(10):

                rind = self.r[i:i + 2]
                rind = np.repeat(rind[:, np.newaxis], 64, axis=1).T
                theta0 = self.theta[note_pos * 64:note_pos * 64 + 64]
                theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)

                if normalized2[j,i] > .80:
                    z = np.ones((64, 2)) * (self.data[11], self.data[note_pos])
                elif normalized2[j,i] > .7:
                    z = np.ones((64, 2)) * (self.data[10], self.data[note_pos])
                elif normalized2[j,i] > .67:
                    z = np.ones((64, 2)) * (10, self.data[note_pos])
                elif normalized2[j,i] > .63:
                    z = np.ones((64, 2)) * (9, self.data[note_pos])
                elif normalized2[j,i] > .6:
                    z = np.ones((64, 2)) * (8, self.data[note_pos])
                elif normalized2[j,i] > .55:
                    z = np.ones((64, 2)) * (7, self.data[note_pos])
                elif normalized2[j,i] > .5:
                    z = np.ones((64, 2)) * (6, self.data[note_pos])
                elif normalized2[j,i] > .45:
                    z = np.ones((64, 2)) * (5, self.data[note_pos])
                elif normalized2[j,i] > .35:
                    z = np.ones((64, 2)) * (4,self.data[note_pos])
                elif normalized2[j,i] > .25:
                    z = np.ones((64, 2)) * (3, self.data[note_pos])
                elif normalized2[j,i] > .15:
                    z = np.ones((64, 2)) * (2, self.data[note_pos])
                elif normalized2[j,i] > .1:
                    z = np.ones((64, 2)) * (1, self.data[note_pos])
                else:
                    z = np.ones((64, 2)) * (0, self.data[note_pos])

                # if normalized2[j,i] > .7:
                #     self.color = "red"
                # elif normalized2[j,i] > .65:
                #     self.color = "#FF4500"
                # elif normalized2[j,i] > .4:
                #     self.color = "yellow"
                # elif normalized2[j,i] > .3:
                #     self.color = "#00FF00"
                # # elif normalized2[j,i] > .3:
                # #     self.color = "#00FFFF"
                # else:
                #     self.color = "white"


                self.ax.pcolormesh(theta0, rind, z, cmap=self.cmap, norm=self.norm, alpha=normalized2[j,i])
        plt.show()
        # self.fig.canvas.draw()
        # # plt.title(chord_name)


    def start_plot(self):


        self.bullseye_plot(self.ax, self.data)



