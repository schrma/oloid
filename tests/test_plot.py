import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import oloid.circle

def test_plot():
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection='3d')

    my_circle1 = oloid.circle.circle([0,1,0],[0,1,0], 5,100)
    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z ** 2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)
    x = my_circle1.get_x()
    y = my_circle1.get_y()
    z = my_circle1.get_z()
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()

    plt.show()