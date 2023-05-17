import matplotlib.pyplot as plt
from numpy import linspace

from lagrange import Point, lagrange_interpolation, lagrange_interpolation_str


vertexes: list[Point] = [
    Point(-4, -1),
    Point(-3, -5),
    Point(-2, 0),
    Point(-1, -2),
    Point(0, 0),
    Point(1, 9),
    Point(4, 12)
]


xp = [p.x for p in vertexes]
yp = [p.y for p in vertexes]


lagrange = lagrange_interpolation(vertexes)

fromx = min(xp)
tox = max(xp)

fromy = min(yp)
toy = max(yp)

print(lagrange_interpolation_str(vertexes))

linex = linspace(fromx, tox, 100)
liney = [lagrange(x=x) for x in linex]


plt.plot(linex, liney)
plt.plot(xp, yp, 'ro')
plt.show()
