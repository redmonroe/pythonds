#chapter1
# 1Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class Fraction(object):

    def __init__(self, top, bottom):
        common = self.gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def __str__(self):
        return f'{self.num}/{self.den}'

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
print(my_fraction.get_num())
print(my_fraction.get_den())