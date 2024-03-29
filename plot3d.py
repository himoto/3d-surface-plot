import matplotlib.pyplot as plt
import numpy as np


class Plot3D(object):
    def __init__(self, x, y, z):
        self.x = x # 1d array
        self.y = y # 1d array
        self.z = z # 2d array

        fig = plt.figure(figsize=(8, 6))
        self.ax = fig.add_subplot(111, projection='3d')

    def surf_plot(self):
        self.ax.plot_surface(
            *np.meshgrid(self.x, self.y), self.z, 
            shade=True, cmap='jet', rstride=1, cstride=1
        )
        self.ax.view_init(azim=-30)

        self.ax.set_xlim(0, 100)
        self.ax.set_xticks([0, 50, 100])
        self.ax.set_xticklabels(['100', '50', '0'])
        
        self.ax.set_ylim(0, 90)
        self.ax.set_yticks([0, 30, 60, 90])
        
        self.ax.set_zlim(0, 3)
        self.ax.set_zticks([0, 1, 2, 3])

        '''
        self.ax.set_xlabel(
            r'$\it{dusp}$'+' mRNA\nknockdown efficiency (%)', labelpad=10
        )
        self.ax.set_ylabel('Time (min)', labelpad=7.5)
        self.ax.set_zlabel(
            r'$\it{c}$'+'-'+r'$\it{fos}$'+' mRNA\nexpression (%)', labelpad=5
        )
        '''


def main():
    '''dusp mRNA knockdown efficiency'''
    x = (1-np.arange(101)/100)*100

    '''Time (min)'''
    y = np.arange(5401) / 60

    '''c-fos mRNA expression'''
    z = np.load('data/z_cFosmRNA.npy')[0].T
    # z = np.load('data/z_cFosmRNA.npy')[1].T

    plt.rcParams['font.size'] = 20
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.it'] = 'Arial:italic'
    plt3d = Plot3D(x, y, z)
    plt3d.surf_plot()

    plt.show()


if __name__ == '__main__':
    main()
