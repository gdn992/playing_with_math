from functools import reduce
import matplotlib.pyplot as plt


class Pont:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


pontok: list[Pont] = [
    Pont(-2, -39),
    Pont(-1, -5),
    Pont(0, 1),
    Pont(1, 3),
    Pont(2, 25)
]


xp = [p[0] for p in pontok]
yp = [p[1] for p in pontok]


def lagrange_interpolacio(pontok: list[Pont]):
    alappolinomok: list[function] = []

    for pont in pontok:
        alappolinomok.append(lambda x: alappolinom(x, pont, pontok) * pont.y)

    def summa(x): return reduce(lambda pn, pn1: pn(x) + pn1(x), alappolinomok)
    return summa


def alappolinom(x, pont: Pont, pontok: list[Pont]):
    Lk = []
    for pontk in pontok:
        if pont.x != pontk.x:
            Lk.append((x-pont.x)/(pontk.x-pont.x))
    return reduce(lambda x, y: x * y, Lk)


lagrange = lagrange_interpolacio(pontok)

plt.plot(lagrange)
plt.plot(xp, yp, 'ro')
plt.axis([-3, 3, -40, 30])
plt.show()
