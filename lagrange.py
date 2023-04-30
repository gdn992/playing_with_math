from functools import reduce
import matplotlib.pyplot as plt
from numpy import linspace


class Pont:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


pontok: list[Pont] = [
    Pont(-2, -39),
    Pont(-1, -5),
    Pont(0, -5),
    Pont(1, 3),
    Pont(2, 25)
]


xp = [p.x for p in pontok]
yp = [p.y for p in pontok]
#     for i, pont in enumerate(pontok):
#         x = pont.x
#         y = pont.y
#         fuggvenyek.append(lambda X, x=x, y=y, pontok=pontok: alappolinom(X, x, y, pontok))


def lagrange_interpolacio(pontok: list[Pont]):
    alappolinomok: list[function] = []

    for i, pont in enumerate(pontok):
        x = pont.x
        y = pont.y
        alappolinomok.append(lambda X, x=x, y=y: alappolinom(X, x, y, pontok))

    def summa(x: float):
        result = 0

        print('-' * 10)
        for polinom in alappolinomok:
            result += polinom(x)
        print('-' * 10)
        return result

    return summa


def alappolinom(X: float, x: float, y: float, pontok: list[Pont]):
    L: float = 1
    Ln: list[str] = []
    for pont in pontok:
        if x != pont.x:
            Ln.append('((x-'+str(pont.x)+')/('+str(x)+'-'+str(pont.x)+'))')
            L *= (X-pont.x)/(x-pont.x)
    print('*'.join(Ln).replace('--', '+'))
    return L * y


lagrange = lagrange_interpolacio(pontok)

fromx = min(xp)
tox = max(xp)

fromy = min(yp)
toy = max(yp)

linex = linspace(fromx, tox, 100)
print(linex)
liney = [lagrange(x=x) for x in linex]


plt.plot(linex, liney)
plt.plot(xp, yp, 'ro')
plt.show()
