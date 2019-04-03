import socket, time
from polinom import Polinom
from complex import Complex

def strToComplex(*args):
    result = []
    for part in args:
        part = complex(part)
        result.append(Complex(part.real, part.imag))
    return result

#host = socket.gethostbyname(socket.gethostname())
host = '127.0.0.1'
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False
print('[Server started]')
print("Waiting for client")

client = None

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[""]/", end="")
        client = addr
        data = data.decode("utf-8")
        print(data)
        wdata = data[1:]
        if (data[0] == 'r'):
            c1, c2, c3 = wdata.split(',')
            coeffs = strToComplex(c1,c2,c3)
            polinom = Polinom(*coeffs)
            roots = polinom.roots()
            roots = str(roots).encode("utf-8")
            s.sendto(roots, client)

        elif (data[0] == 'v'):
            c1, c2, c3, value = wdata.split(',')
            coeffs = strToComplex(c1,c2,c3)
            polinom = Polinom(*coeffs)
            value = complex(value)
            result = polinom.value(Complex(value.real, value.imag))
            s.sendto(str(result).encode('utf-8'), client)
    except:
        s.close()
        quit = True












