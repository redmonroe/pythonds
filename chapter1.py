#chapter1
# 1Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class Fraction(object):

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other_frac):
        newnum = self.num * other_frac.den + self.den * other_frac.num
        newden = self.den * other_frac.den
        common = self.gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def gcd(self, num, den):
        while num % den != 0:
            oldm = num
            oldn = den
            num = oldn
            den = oldm % oldn
        
        return den


my_fraction = Fraction(1, 2)
my_fraction2 = Fraction(1, 4) 
print(my_fraction + my_fraction2)