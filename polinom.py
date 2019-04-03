



from complex import Complex, sqrt
class Polinom:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
        self.arr = [self.a, self.b, self.c]

    def value(self, x):
        return self.a*(x*x) + self.b*x + self.c

    def roots(self):
        D = self.b*self.b - 4*self.a*self.c
        if D > 0:
            x1 = (-1*self.b + sqrt(D)) /(2 * self.a)
            x2 = (-1*self.b - sqrt(D)) /(2 * self.a)
            return [x1.__str__(), x2.__str__()]
        elif D == 0:
            return -1*self.b/(2*self.a)
        else:
            return None

    def __str__(self):
        result = ''
        coeffs = []
        for index, k in enumerate(self.arr):
            if k > 0 and index != 0:
                coeffs.append(' + ' + str(k))
            elif index == 0 or k < 0:
                coeffs.append(str(k))
            elif k == 0:
                coeffs.append(0)
        if self.a == self.b == self.c == 0:
            return 0
        for index, k in enumerate(coeffs):
            if k != 0:
                if index == 0:
                    result += k + 'x^2'
                elif index == 1:
                    result += k + 'x'
                else:
                    result += k
        return result
    def __repr__(self):
        return self.__str__()



obj = Polinom(1,2,3)
print(obj.value(5))








