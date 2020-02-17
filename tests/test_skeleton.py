# -*- coding: utf-8 -*-

import pytest
from oloid.skeleton import fib

__author__ = "marcoHP"
__copyright__ = "marcoHP"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
