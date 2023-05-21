from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from numpy import linspace

from src.components.pointListWidget import PointListWidget
from src.math.lagrange import Point, lagrange_interpolation, lagrange_interpolation_str


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class LagrangeWindow(QWidget):
    points = []

    def __init__(self):
        super(LagrangeWindow, self).__init__()
        self.canvas = MplCanvas(self)

        self.points: list[Point] = [
            Point(-4, -1),
            Point(-3, -5),
            Point(-2, 0),
            Point(-1, -2),
            Point(0, 0),
            Point(1, 9),
            Point(4, 12)
        ]

        layout = QtWidgets.QHBoxLayout(self)

        self.point_list = PointListWidget(self.calculate, initial_points=self.points, )

        layout.addWidget(self.point_list, 1)
        layout.addWidget(self.canvas, 1)

        self.setLayout(layout)
        self.calculate()

    def calculate(self, _=''):
        xp = [p.x for p in self.points]
        yp = [p.y for p in self.points]

        lagrange = lagrange_interpolation(self.points)

        if len(xp) == 0:
            self.canvas.axes.clear()
            self.canvas.draw()
            return

        from_x = min(xp)
        to_x = max(xp)

        print(lagrange_interpolation_str(self.points))

        line_x = linspace(start=from_x, stop=to_x, num=100)
        line_y = [lagrange(x=x) for x in line_x]

        self.canvas.axes.clear()
        self.canvas.axes.scatter(xp, yp, c='green')
        self.canvas.axes.plot(line_x, line_y)
        self.canvas.axes.plot(line_x, line_y)
        self.canvas.draw()
