#chapter1
# 1Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class Fraction(object):

    def __init__(self, top, bottom):
        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
             top = -top
             bottom = abs(bottom)
        if not isinstance(top, int):
            valEr = ValueError(f'{top} is not an integer.')
            raise valEr
        elif not isinstance(bottom, int):
            valEr = ValueError(f'{bottom} is not an integer.')
            raise valEr
        else:
            print(type(top), top, type(bottom), bottom)
            common = self.gcd(top, bottom)
            self.num = top//common
            self.den = bottom//common

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'Fraction({self.num}/{self.den})'

    def __add__(self, other_frac):
        newnum = self.num * other_frac.den + self.den * other_frac.num
        newden = self.den * other_frac.den
        return Fraction(newnum, newden)

    def __sub__(self, other_frac):
        newnum = self.num * other_frac.den - self.den * other_frac.num
        newden = self.den * other_frac.den
        return Fraction(newnum, newden)

    def __mul__(self, other_frac):
        newnum = self.num * other_frac.num
        newden = self.den * other_frac.den
        return Fraction(newnum, newden)

    def __truediv__(self, other_frac):
        newnum = self.num * other_frac.den
        newden = self.den * other_frac.num
        return Fraction(newnum, newden)

    def __eq__(self, other_frac):
        firstnum = self.num * other_frac.den
        secondnum = other_frac.num * self.den

        return firstnum == secondnum

    def __gt__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = self.den * other_frac.num
        return first_num > second_num
    
    def __lt__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = self.den * other_frac.num
        return first_num < second_num

    def __ge__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = self.den * other_frac.num
        return first_num >= second_num
 
    def __le__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = self.den * other_frac.num
        return first_num <= second_num
    
    def __ne__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = self.den * other_frac.num
        return first_num != second_num

    def __radd__(self):
        __radd__ == __add__
    
    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def gcd(self, num, den):
        while num % den != 0:
            oldm = num
            oldn = den
            num = oldn
            den = oldm % oldn
        
        return den


my_fraction = Fraction(1, 5)
my_fraction2 = Fraction(1, 10) 
my_fraction3 = Fraction(1, 10) 
neg_fraction = Fraction(-1, 99)
test_frac = my_fraction + my_fraction2
test_sub = my_fraction2 - my_fraction
test_mul = my_fraction2 * my_fraction
test_div = my_fraction2 / my_fraction
test_gt = my_fraction2 > my_fraction
test_lt = my_fraction2 < my_fraction
test_ge = my_fraction2 >= my_fraction
test_ge2 = my_fraction2 >= my_fraction3
test_le = my_fraction2 >= my_fraction3
test_ne = my_fraction2 != my_fraction3
print(my_fraction.__repr__())
print('addition test:', test_frac)
print('subtraction test:', test_sub)
print('multiplication test:', test_mul)
print('division test:', test_div)
print('greater than test:', test_gt)
print('less than test:', test_lt)
print('ge test:', test_ge)
print('ge2 test:', test_ge2)
print('le test:', test_le)
print(f'ne test {my_fraction2} & {my_fraction3}:', test_ne)
print('abs test:', neg_fraction)

dec = 1.1
my_fraction4 = Fraction(dec, 10) 
print(my_fraction4)