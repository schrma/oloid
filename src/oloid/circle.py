
class circle:
    def __init__(self,center_point, normal_vector, radius=1,nr_of_points=100):
        self.center_point = center_point
        self.normal_vector = normal_vector
        self.radius = radius
        self.nr_of_points = nr_of_points

    def get_x(self):
        [x,y,z] = self.calculate()
        return x

    def get_y(self):
        [x,y,z] = self.calculate()
        return y

    def get_z(self):
        x,y,z = self.calculate()
        return z

    def calculate(self):
        x = 10
        y = 20
        z = 100
        return x,y,z
