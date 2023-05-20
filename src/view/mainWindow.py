from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStackedWidget

from src.math.lagrange import Point
from src.model.HeaderButtonComponent import HeaderButtonComponent
from src.view.contentWindow import ContentWindow
from src.view.headerWindow import HeaderWindow
from src.view.lagrangeWindow import LagrangeWindow

points: list[Point] = [
    Point(-4, -1),
    Point(-3, -5),
    Point(-2, 0),
    Point(-1, -2),
    Point(0, 0),
    Point(1, 9),
    Point(4, 12)
]


class MainWindow(QWidget):
    content: QStackedWidget

    components: list[HeaderButtonComponent] = [
        HeaderButtonComponent(component=LagrangeWindow, name='1Lagrange interpolation'),
        HeaderButtonComponent(component=ContentWindow, name='2Lagrange interpolation'),
        HeaderButtonComponent(component=LagrangeWindow, name='3Lagrange interpolation')
    ]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)

        self.header = HeaderWindow(self.components, self.header_button_click)
        self.content = QtWidgets.QStackedWidget(self)

        self.content.addWidget(self.components[0].component())

        layout = QVBoxLayout(self)
        layout.addWidget(self.header, 0)
        layout.addWidget(self.content, 1)

        self.setLayout(layout)
        self.show()

    def header_button_click(self, header_component: HeaderButtonComponent):
        self.content.removeWidget(self.content.currentWidget())
        self.content.addWidget(header_component.component())
