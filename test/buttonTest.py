from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QCheckBox,\
	QRadioButton,QMenu,QAction,QButtonGroup
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

# QRadioButton  用户可以选择之一
def radioButtonHandler(btn):
	print('radioButtonHandler : ',btn.isChecked())
def zuButtonToggledHandler(id,t):
	print('zu: ',id,t)
def radioButtonTest(p):
	btn1 = QRadioButton("男")
	btn1.setChecked(True)
	# btn1.setCheckable(False)
	btn1.toggled.connect(lambda:radioButtonHandler(btn1))
	btn1.setParent(p)
	btn1.setGeometry(10,20,80,30)
	btn1.setShortcut("Alt+M")  # 设置快捷
	btn2 = QRadioButton("女")
	btn2.setParent(p)
	btn2.setGeometry(10,60,80,30)
	btn2.setShortcut("Alt+F")  # 设置快捷
	# 创建分组
	zu1 = QButtonGroup(p)  # 创建一个按钮分组实例
	# 参数2 给按钮设置一个id,不同分组的id可以重复
	# 如果id为-1，则将为该按钮分配一个id。自动分配的ID保证为负数，从-2开始。
	zu1.addButton(btn1, 1)  # 给按钮分组实例添加按钮
	zu1.addButton(btn2, 2)  # 给按钮分组实例添加按钮
	zu1.setExclusive(False) #是否独占
	zu1.buttonToggled[int,bool].connect(zuButtonToggledHandler)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()
	# menuPushButton(w)
	# pushButtonTest(w)
	radioButtonTest(w)
	w.show()
	sys.exit(app.exec_())

