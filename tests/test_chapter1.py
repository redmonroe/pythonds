import pytest
from chapter1 import Fraction
# from chapter1 import sum


MY_NUMERATOR1 = 1
MY_NUMERATOR2 = 1
MY_DEN1 = 2
MY_DEN2 = 4

@pytest.fixture
def fraction():
    return Fraction()

def test_init():
    fr = Fraction(MY_NUMERATOR1, MY_DEN1)
    assert isinstance(fr, Fraction) == True

def test_add():
    # answer = fraction.__add__(MY_NUMERATOR1, MY_DEN1)
    # assert answer
    pass

#     fr = Fraction(MY_NUMERATOR1, MY_DEN1)
#     fr2 = Fraction(MY_NUMERATOR2, MY_DEN2)
#     print(fr + fr2)
#     assert fr + fr2 == Fraction(3, 4)