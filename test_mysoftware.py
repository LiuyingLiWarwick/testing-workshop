
from mysoftware import *


def test_square_integers():
    assert square(2) ==4
    assert square(0) ==0
    assert square(-1) == 1
    assert square(3) == 9


def test_coulumb():
    assert coulomb (1) == 1
    assert coulomb (2) == 0.5