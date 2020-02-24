import numpy as np
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Line3D

class circle(Line3D):
    def __init__(self,center_point, normal_vector, radius=1,nr_of_points=100):
        self.center_point = center_point
        self.normal_vector = normal_vector
        self.radius = radius
        self.nr_of_points = nr_of_points
        Line3D.__init__(self, [], [], [], label='parametric curve')


    def draw(self, renderer):
        x,y,z = self.calculate()
        xs3d, ys3d, zs3d = x,y,z
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_data_3d(x, y,z)
        Line3D.draw(self, renderer)

    def get_x(self):
        x,y,z = self.calculate()
        return x

    def get_y(self):
        x,y,z = self.calculate()
        return y

    def get_z(self):
        x,y,z = self.calculate()
        return z

    def calculate(self):

        theta = np.linspace(0, 2 * np.pi, self.nr_of_points)
        z = 0
        x = self.radius * np.sin(theta)
        y = self.radius * np.cos(theta)
        return x,y,z
