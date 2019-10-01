from PyQt5.QtWidgets import QApplication,QWidget
from MainWidget import MianWiget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MianWiget()
    widget.show()
    sys.exit(app.exec())
