from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QCheckBox,QRadioButton,QMenu,QAction
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize
import sys
#pushButton
def pushBtnToggle(t):
	print('pushBtnToggle:',t)
def btnstate(btn):
	if btn.isChecked():
		print("button pressed")
	else:
		print("button released")
def pushButtonTest(p):
	btn1 = QPushButton("Button1")
	btn1.setParent(p)
	# 按钮是否可选中
	btn1.setCheckable(True)
	# 设置按钮是否使能
	# btn1.setEnabled(False)
	# (两种状态之间)切换事件
	btn1.toggled[bool].connect(lambda t: pushBtnToggle(t))
	# 点击事件
	btn1.clicked.connect(lambda :btnstate(btn1))
	icon = QIcon()
	icon.addPixmap(QPixmap('./image/img1.jpeg'),QIcon.Normal,QIcon.Off)
	icon.addPixmap(QPixmap('./image/img2.jpeg'),QIcon.Normal,QIcon.On)

	btn1.setIcon(icon)
	btn1.setIconSize(QSize(40,40))

#pushbutton创建菜单栏
def menuHandler(action,btn):
	print(action.text())
	btn.setText(action.text())
def menuPushButton(p):
	# 菜单
	pMenu = QMenu();
	pMenu.addAction("设置");
	pMenu.addAction("版本检测");
	# 下划线
	pMenu.addSeparator();
	pMenu.addAction("关于我们");
	pMenu.addAction("退出");
	# 按钮
	pButton =QPushButton(p);
	pButton.setGeometry(10,20,100,30)
	pButton.setText("主菜单");
	# 设置菜单
	pButton.setMenu(pMenu);
	pMenu.triggered[QAction].connect(lambda action:menuHandler(action,pButton))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()
	# menuPushButton(w)
	pushButtonTest(w)
	w.show()
	sys.exit(app.exec_())

