
from cmath import sqrt as msq
class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imag = im


    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if isinstance(other, Complex):
            real= self.real* other.real- (self.imag*other.imag)
            imag= self.imag*other.real+ self.real* other.imag
            return Complex(real, imag)
        else:
            return Complex(self.real* other, self.imag* other)

    def __sub__(self, other):
        return self + (other*(-1))


    def __truediv__(self, other):
        if isinstance(other, Complex):
            res = self * Complex(other.real, -1*other.imag)
            diviver = other.real**2 + other.imag**2
            res.imag /= diviver
            res.real/= diviver
            return res
        else:
            return Complex(self.real* other + self.imag * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        res = '(' + str(self.real)
        res = res + ('+' if self.imag> 0 else '')
        res = res + ((str(self.imag) + 'i') if self.imag!= 0 else '')
        res += ')'
        return res

    def __pow__(self, power):
        begin = self
        res = self
        while power != 1:
            res = res * begin
            power -= 1
        return res

    def __complex__(self):
        a = complex(self.real, self.imag)
        return a
    def __gt__(self, other):
        return True
    def __repr__(self):
        return self.__str__()

def sqrt(number):
    if isinstance(number, Complex):
        return msq(complex(number))
        



#(a + bi)/(c+di) = (a+bi)(c-di)/(cc+dd)


