from functools import partial
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from src.model.HeaderButtonComponent import HeaderButtonComponent


class HeaderWindow(QWidget):
    def __init__(self, header_button_components: list[HeaderButtonComponent], button_click: callable):
        super(HeaderWindow, self).__init__()
        layout = QtWidgets.QHBoxLayout(self)

        self.buttons = QtWidgets.QButtonGroup(self)

        for header_button_component in header_button_components:
            button = QtWidgets.QPushButton()
            self.buttons.addButton(button)

            button.setText(header_button_component.name)
            button.clicked.connect(partial(button_click, header_button_component))

            layout.addWidget(button)

        self.setLayout(layout)
