import pytest
from chapter1 import Fraction
# from chapter1 import sum


MY_NUMERATOR1 = 1
MY_NUMERATOR2 = 2
MY_DEN1 = 2
MY_DEN2 = 4

def test_init():
    fr = Fraction(MY_NUMERATOR1, MY_DEN1)
    assert isinstance(fr, Fraction) == True