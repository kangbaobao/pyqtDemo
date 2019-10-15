from PyQt5.QtWidgets import QApplication,QWidget
import  sys
from mianWin import MainWidget
if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWidget()
	w.show()
	sys.exit(app.exec_())


