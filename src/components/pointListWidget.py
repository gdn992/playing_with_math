from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton

from src.components.pointWidget import PointWidget
from src.math.lagrange import Point


class PointListWidget(QWidget):
    points: list[Point]

    def __init__(self, initial_points: list[Point] = None):
        super(PointListWidget, self).__init__()
        # set vertical layout
        self.setLayout(QtWidgets.QVBoxLayout(self))

        # created AddButton and connected to the layout
        self.add_button = QPushButton(self)
        self.add_button.setIcon(QIcon('src/icons/plus.png'))
        self.add_button.clicked.connect(self.add_point)
        self.layout().addWidget(self.add_button)

        # created widget for the points
        self.points_widget = QWidget(self)
        self.points_widget.setLayout(QVBoxLayout())

        if initial_points is None:
            initial_points = []
        self.points = initial_points

        self.build_points()
        self.layout().addWidget(self.points_widget)

    def build_points(self):
        for index, point in enumerate(self.points):
            self.points_widget.layout().addWidget(
                PointWidget(
                    remove_button_click=partial(self.remove_point, index),
                    point=point,
                    spin_x_changed=partial(self.spin_x_changed, index),
                    spin_y_changed=self.spin_y_changed,
                ))

    def remove_points(self):
        for index in range(self.points_widget.layout().count()):
            item = self.points_widget.layout().itemAt(index)
            if item is not None:
                item.widget().deleteLater()

    def rebuild_points(self):
        self.remove_points()
        self.build_points()

    def remove_point(self, index: int):
        self.points.pop(index)
        self.rebuild_points()

    def add_point(self, x=0.0, y=0.0):
        self.points.append(Point(x=x, y=y))
        self.rebuild_points()

    def spin_x_changed(self, index: int, value: float = 0.0):
        self.points[index].x = value
        self.rebuild_points()

    def spin_y_changed(self, index: int, value: float = 0.0):
        self.points[index].y = value
        self.rebuild_points()
