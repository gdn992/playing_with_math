from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QWidget
from PyQt5 import QtWidgets

from src.model.HeaderButtonComponent import HeaderButtonComponent


class ContentWindow(QWidget):

    def __init__(self):
        super(ContentWindow, self).__init__()
        self.button_group = QtWidgets.QButtonGroup(self)
        self.label = QtWidgets.QLabel(self)
        self.label.setText('content label')