import matplotlib.pyplot as plt
from numpy import linspace

from lagrange import Vertex, lagrange_interpolation, lagrange_interpolation_str


vertexes: list[Vertex] = [
    Vertex(-4, -1),
    Vertex(-3, -5),
    Vertex(-2, 0),
    Vertex(-1, -2),
    Vertex(0, 0),
    Vertex(1, 9),
    Vertex(4, 12)
]


xp = [p.x for p in vertexes]
yp = [p.y for p in vertexes]


lagrange = lagrange_interpolation(vertexes)

fromx = min(xp)
tox = max(xp)

fromy = min(yp)
toy = max(yp)

res = lagrange_interpolation_str(vertexes)
print(res)
linex = linspace(fromx, tox, 100)
liney = [lagrange(x=x) for x in linex]


plt.plot(linex, liney)
plt.plot(xp, yp, 'ro')
plt.show()
