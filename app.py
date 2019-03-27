
from polinom import Polinom
from complex import Complex

pol = Polinom(0, 0, 0)
class Application():
    def run(self):
        while True:
            print('1 - input new Polinom')
            print('2 - roots')
            print('3 - value')
            print('4 - show polinom')
            print('5 - exit')
            choice = int(input())
            if choice == 1:
                print('1 - complex or 2 - double')
                ch = int(input())
                if ch == 2:
                    p = [float(i) for i in input().split()]
                else:
                    p = [complex(i) for i in input().split()]
                    print(p)
                    p = [Complex(i.real, i.imag) for i in p]
                    print([(i.real, i.imag) for i in p])
                pol = Polinom(*p)
                print('polinom created')
                print(pol)
            elif choice == 2:
                print(pol.roots())
            elif choice == 3:
                value = complex(input())
                value = Complex(value.real, value.imag)
                print(pol.value(value))
            elif choice == 4:
                print(pol)
            elif choice == 5:
                break




