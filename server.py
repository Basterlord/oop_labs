import socket, time
from polinom import Polinom
from complex import Complex

import socket, time

#host = socket.gethostbyname(socket.gethostname())
host = '127.0.0.1'
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False
print('[Server started]')
client = None

while not quit:
    print("Waiting for client")

    data, addr = s.recvfrom(1024)

    print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[""]/", end="")
    client = addr
    data = data.decode("utf-8")
    print(data)
    wdata = data[1:]
    if (data[0] == 'r'):
        c1, c2, c3 = wdata.split(',')
        c1, c2, c3 = [complex(i) for i in (c1, c2, c3)]
        coeffs = [Complex(i.real, i.imag) for i in (c1, c2, c3)]
        polinom = Polinom(*coeffs)
        roots = polinom.roots()
        print(roots)
        roots = str(roots).encode("utf-8")
        s.sendto(roots, client)

    elif (data[0] == 'v'):
        c1, c2, c3, value = wdata.split(',')
        c1, c2, c3 = [complex(i) for i in (c1, c2, c3)]
        coeffs = [Complex(i.real, i.imag) for i in (c1, c2, c3)]
        polinom = Polinom(*coeffs)
        value = complex(value)
        result = polinom.value(Complex(value.real, value.imag))
        print(result)
        s.sendto(str(result).encode('utf-8'), client)
s.close()












