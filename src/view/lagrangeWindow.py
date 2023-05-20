import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
from numpy import linspace

from src.math.lagrange import Point, lagrange_interpolation, lagrange_interpolation_str


class LagrangeWindow(QWidget):
    points = []

    def __init__(self):
        super(LagrangeWindow, self).__init__()
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
        self.setLayout(layout)

        self.button = QPushButton("lagrange interpolation ", self)
        self.button.setGeometry(150, 150, 100, 50)
        self.button.clicked.connect(self.calculate_button_click)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def calculate_button_click(self, a2):
        print(self, a2)

        xp = [p.x for p in self.points]
        yp = [p.y for p in self.points]

        lagrange = lagrange_interpolation(self.points)

        from_x = min(xp)
        to_x = max(xp)

        print(lagrange_interpolation_str(self.points))

        line_x = linspace(start=from_x, stop=to_x, num=100)
        line_y = [lagrange(x=x) for x in line_x]

        plt.plot(line_x, line_y)
        plt.plot(xp, yp, 'ro')
        plt.show()
