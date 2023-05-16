import matplotlib.pyplot as plt
from numpy import linspace

from lagrange import Point, lagrange_interpolation, lagrange_interpolation_str


vertexes: list[Point] = [
    Point(-2, -39),
    Point(-1, -5),
    Point(0, 100),
    Point(1, -5),
    Point(2, 3),
    Point(3, 25)
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
