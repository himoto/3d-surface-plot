import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Plot3D(object):
    def __init__(self, x, y, z):
        self.x = x # 1d array
        self.y = y # 1d array
        self.z = z # 2d array

        self.fig = plt.figure(figsize=(8,6))
        self.ax = Axes3D(self.fig)

    def surf_plot(self):
        (self.X,self.Y) = np.meshgrid(self.x,self.y)
        self.Z = self.z

        self.ax.plot_surface(self.X,self.Y,self.Z,shade=True,cmap='jet',rstride=1,cstride=1)
        self.ax.view_init(azim=-30)

        self.ax.set_xlim(0,100)
        self.ax.set_xticks([0,50,100])
        self.ax.set_xticklabels(['100','50','0'])
        self.ax.set_xlabel(r'$\it{dusp}$'+' mRNA\nknockdown efficiency (%)',labelpad=10)
        self.ax.set_ylim(0,90)
        self.ax.set_yticks([0,30,60,90])
        self.ax.set_ylabel('Time (min)',labelpad=7.5)
        self.ax.set_zlim(0,3)
        self.ax.set_zticks([0,1,2,3])
        self.ax.set_zlabel(r'$\it{c}$'+'-'+r'$\it{fos}$'+' mRNA\nexpression (%)',labelpad=5)


def surface():
    '''dusp mRNA knockdown efficiency'''
    x = (1-np.arange(101)/100)*100

    '''Time (min)'''
    y = np.arange(5401)/60

    '''c-fos mRNA expression'''
    z = np.load('data/z_cFosmRNA_egf.npy')
    # z = np.load('data/z_cFosmRNA_hrg.npy')

    plt.rcParams['font.size'] = 15
    plt.rcParams['font.family'] = 'Arial'
    plt3d = Plot3D(x, y, z)
    plt3d.surf_plot()

    plt.show()


if __name__ == '__main__':
    surface()