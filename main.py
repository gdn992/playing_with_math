import sys
from PyQt5.QtWidgets import QApplication

from src.view.mainWindow import MainWindow


def window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


window()
