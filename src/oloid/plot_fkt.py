import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D, proj3d
import matplotlib.pyplot as plt
import numpy as np
import itertools

import oloid.circle

fig = plt.figure()
ax = fig.gca(projection='3d')

# #dibujar cubo
r = [-1, 1]
for s, e in itertools.combinations(np.array(list(itertools.product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="b")

#dibujar punto
ax.scatter([0],[0],[0],color="g",s=100)


class Arrow3D(mpatches.FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        mpatches.FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        mpatches.FancyArrowPatch.draw(self, renderer)


#m=float(raw_input())
a = Arrow3D([0,0],[0,1],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
b = Arrow3D([0,-1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
c = Arrow3D([0,0],[0,0],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
d = Arrow3D([0,0],[0,0],[0,-1], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
e = Arrow3D([0,1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="c")
f = Arrow3D([0,0],[0,-0.5],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="m")

my_circle = oloid.circle.circle([0, 0, 0], [1, 2, 3], 2, 100)

ax.add_artist(my_circle)
ax.add_artist(a)
ax.add_artist(b)
ax.add_artist(c)
ax.add_artist(d)
ax.add_artist(e)
ax.add_artist(f)
ax.legend()
plt.show()