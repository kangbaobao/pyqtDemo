# 内置信号连接槽函数
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# from PyQt5.QtGui import
import sys
from PyQt5.QtCore import QRect,QPoint,QSize


def btnAtion():
	print('按钮被点击了')
if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()
	btn = QPushButton()
	btn.setText("button1")
	btn.setParent(w)
	btn.setGeometry(QRect(50,10,80,30))
	#btn.clicked.connect(w.close)#(lambda :w.close())
	# btn.clicked.connect(app.quit)
	btn.clicked.connect(btnAtion)#(lambda : btnAtion())
	w.show()
	sys.exit(app.exec_())


