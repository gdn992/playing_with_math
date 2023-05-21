from PyQt5.QtWidgets import QWidget, QButtonGroup, QLabel


class ContentWindow(QWidget):
    def __init__(self):
        super(ContentWindow, self).__init__()
        self.button_group = QButtonGroup(self)
        self.label = QLabel(self)
        self.label.setText('content label')
