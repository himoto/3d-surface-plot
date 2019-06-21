# 3d-surface-plot

![Picture1](https://user-images.githubusercontent.com/31299606/59900035-db982380-9431-11e9-9603-8f2cdbc0a8e4.png)

Simulated effects of various degrees of dusp knockdown on EGF-induced and HRG-induced *c-fos* mRNA expression.
- [Nakakuki, T. *et al.* Ligand-specific c-Fos expression emerges from the spatiotemporal control of ErbB network dynamics. *Cell* **141**, 884–896 (2010).](https://doi.org/10.1016/j.cell.2010.03.054)

## Create a surface plot
```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

%matplotlib inline

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

def main():
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
    main()
```

## Installation
    $ git clone https://github.com/himoto/3d-surface-plot.git
## License
[MIT](/LICENSE)
