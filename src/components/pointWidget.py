from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDoubleSpinBox, QPushButton

from src.math.lagrange import Point


class PointWidget(QWidget):

    def __init__(
            self,
            remove_button_click: callable,
            spin_x_changed: callable,
            spin_y_changed: callable,
            point: Point = None
    ):
        super(PointWidget, self).__init__()
        if point is None:
            point = Point(0, 0)
        self.setLayout(QHBoxLayout(self))

        self.spin_x = QDoubleSpinBox(self)
        self.spin_x.setMinimum(-100.0)
        self.spin_x.setValue(point.x)
        self.spin_x.valueChanged.connect(spin_x_changed)
        self.layout().addWidget(self.spin_x)

        self.spin_y = QDoubleSpinBox(self)
        self.spin_y.setMinimum(-100.0)
        self.spin_y.setValue(point.y)
        self.spin_y.valueChanged.connect(spin_y_changed)
        self.layout().addWidget(self.spin_y)

        self.remove_button = QPushButton(self)
        self.remove_button.setIcon(QIcon('src/icons/X.png'))
        self.remove_button.clicked.connect(remove_button_click)
        self.layout().addWidget(self.remove_button)
