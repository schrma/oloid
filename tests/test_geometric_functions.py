import pytest
import numpy as np
import oloid.geometric_functions


def test_get_orthogonal_raise():
    with pytest.raises(TypeError):
        oloid.geometric_functions.get_orthogonal_vector([0,1,2])

@pytest.mark.parametrize("input_vector", [(np.array([0, 1, 0])),
                                                   (np.array([1, 0, 0])),
                                                   (np.array([0, 0, 1])),
                                                   (np.array([2, 1, 3])),
                                                   (np.array([1, 1, 1])),
                                                   ])
def test_get_orthogonal(input_vector):
    ortho_vector = oloid.geometric_functions.get_orthogonal_vector(np.array(input_vector))
    print(ortho_vector)
    assert np.dot(input_vector, ortho_vector) == 0