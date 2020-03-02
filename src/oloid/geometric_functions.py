import numpy as np


def get_orthogonal_vector(input_vector):
    if not isinstance(input_vector, (np.ndarray)):
        raise TypeError('input vector is from type' + type(input_vector))

    vector_length = input_vector.shape[0]

    if vector_length == 3:
        n0 = input_vector[0]
        n1 = input_vector[1]
        n2 = input_vector[2]
        if n0 != 0:
            x0 = -(n1+n2)/n0
            x1 = 1
            x2 = 1
        elif n1 != 0:
            x0 = 1
            x1 = -(n0+n2)/n1
            x2 = 1
        else:
            x0 = 1
            x1 = 1
            x2 = -(n0+n1)/n2
        return np.array([x0,x1,x2])

