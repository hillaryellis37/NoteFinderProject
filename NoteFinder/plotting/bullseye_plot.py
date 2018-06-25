import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],
                  projection='polar', facecolor='#d5de9c')
data = np.array(range(17)) + 1

class Plot:
    def __init__(self, fig=fig, data=data, chord_name=False, amp_dict=False):

        self.data = data

        # Make a figure and axes with dimensions as desired.

        self.fig = fig
        self.ax = ax
        self.chord_name = chord_name
        self.amp_dict = amp_dict

        # Set the colormap and norm to correspond to the data for which
        # the colorbar will be used.
        self.cmap = mpl.cm.jet
        self.norm = mpl.colors.Normalize(vmin=1, vmax=15)


    def bullseye_plot(self, ax, data, segBold=None, cmap=None, norm=None):

        if segBold is None:
            segBold = []

        linewidth = 2
        data = np.array(data).ravel()

        if cmap is None:
            cmap = plt.cm.viridis

        if norm is None:
            norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max())

        theta = np.linspace(0, 2*np.pi, 768)

        r = np.linspace(0.0, 1, 11)
        print("r= ", r)
        print(r.shape)

        for i in range(r.shape[0]):
            ax.plot(theta, np.repeat(r[i], theta.shape), '-k', linewidth=1)

        for i in range(12):
            theta_i = i*30*np.pi/180

            ax.plot([theta_i, theta_i], [r[0], 1], '-k', linewidth=.5)

        print("norm = ",norm)

        for i in range(len(r)):

            r0 = r[i:i+2]
            r0 = np.repeat(r0[:, np.newaxis], 64, axis=1).T

            for i in range(12):

                theta0 = theta[i*64:i*64+64]
                theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)

                z = np.ones((64, 2))*data[i]

                ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm, alpha=0.1)
                if i+1 in segBold:
                    ax.plot(theta0, r0, '-k', lw=linewidth+2)
                    ax.plot(theta0[0], [r[2], r[3]], '-k', lw=linewidth+1)
                    ax.plot(theta0[-1], [r[2], r[3]], '-k', lw=linewidth+1)
        oct = 1
        note_int = 1

        rind = r[oct:oct+2]
        rind = np.repeat(rind[:, np.newaxis], 64, axis=1).T
        theta0 = theta[note_int * 64:note_int * 64 + 64]
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        # print("theta0 =", theta0)
        z = np.ones((64, 2)) * data[note_int]
        # print("z = ", z)
        ax.pcolormesh(theta0, rind, z, cmap=cmap, norm=norm, alpha=1)


        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        ax.set_ylim([0, 1])

        ax.set_yticks(np.linspace(0, 1, 11))
        ax.set_yticklabels(range(10))
        ax.set_xticks(np.linspace(0, 12*60*np.pi/360, 13))
        ax.set_xticklabels(notes)


    def start_plot(self):

        ax = self.ax
        data = self.data

        self.bullseye_plot(ax, data, cmap=self.cmap, norm=self.norm)

        plt.show()
#
# # Create the fake data
# data = np.array(range(17)) + 1
#
#
# # Make a figure and axes with dimensions as desired.
# fig, ax = plt.subplots(figsize=(15, 10), nrows=1, ncols=3,
#                        subplot_kw=dict(projection='polar'))
# fig.canvas.set_window_title('Left Ventricle Bulls Eyes (AHA)')
#
#
# # Create the axis for the colorbars
#
#
# axl = fig.add_axes([0.14, 0.15, 0.2, 0.05])
# axl2 = fig.add_axes([0.41, 0.15, 0.2, 0.05])
# axl3 = fig.add_axes([0.69, 0.15, 0.2, 0.05])
#
#
# # Set the colormap and norm to correspond to the data for which
# # the colorbar will be used.
# cmap = mpl.cm.jet
# norm = mpl.colors.Normalize(vmin=1, vmax=15)
#
# cmap2 = mpl.cm.cool
# norm2 = mpl.colors.Normalize(vmin=1, vmax=17)
#
#
# cmap3 = mpl.colors.ListedColormap(['r', 'g', 'b', 'c'])
# cmap3.set_over('0.35')
# cmap3.set_under('0.75')
#
# # If a ListedColormap is used, the length of the bounds array must be
# # one greater than the length of the color list.  The bounds must be
# # monotonically increasing.
# bounds = [2, 3, 7, 9, 15]
# norm3 = mpl.colors.BoundaryNorm(bounds, cmap3.N)
#
#
#
# bullseye_plot(ax, data, cmap=cmap, norm=norm)
#
# # bullseye_plot(ax[0], data, segBold=[3, 5, 6, 11, 12, 16],
# #               cmap=cmap, norm=norm)
# # ax[0].set_title('Segments [3,5,6,11,12,16] in bold')
#
# plt.show()