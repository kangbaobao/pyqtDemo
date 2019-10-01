from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QHBoxLayout,QGridLayout,QPushButton
from  PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette,QColor,QFont
from  PyQt5.Qt import Qt

class MianWiget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent);
		self.setFixedSize(QSize(250,330))
		palette = QPalette()
		palette.setColor(QPalette.Background,QColor().fromRgb(68,69,73))
		self.setPalette(palette)
		self.strList = ['C','+/-','%','/',
						'7', '8', '9', '*',
						'4', '5', '6', '-',
						'1', '2', '3', '+',
						'0', '.', '=',
						];
		self.setupUI()

	def setupUI(self):
		# 主布局
		mainLayout = QVBoxLayout()
		#设置mainLayout left top,right,bottom 为0
		mainLayout.setContentsMargins(0,0,0,0)
		self.setLayout(mainLayout)

		#toplayout 展示上面的输入内容
		topLayout = QHBoxLayout()
		topLayout.setContentsMargins(5,5,5,0)
		mainLayout.addLayout(topLayout)
		self.showLab = QLabel('0')
		font = QFont()
		font.setFamily('宋体')
		font.setBold(True)
		font.setPointSize(40)

		self.showLab.setFont(font)
		self.showLab.setFixedHeight(40)
		topLayout.addWidget(self.showLab)

		self.showLab.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
		palette = QPalette()
		palette.setColor(QPalette.Foreground,Qt.white)
		self.showLab.setPalette(palette)
		self.showLab.setObjectName("showLab")
		# self.showLab.setStyleSheet(
		# 	"#showLab {background-color:rgb(255,0,0);border-radius:0px;} ")#

		bottomLayout = QGridLayout()
		# bottomLayout.setSpacing(5)
		bottomLayout.setContentsMargins(5,5,5,0)
		mainLayout.addLayout(bottomLayout,1)
		# mainLayout.addStretch(1)

		for index,value in enumerate(self.strList):
			btn = QPushButton()
			btn.setText(value)
			btn.setObjectName(value)
			btn.setMinimumHeight(50)

			if index %4 == 3 or index == 18:
				btn.setStyleSheet(
					"QPushButton {background-color:rgb(246,154,46);color:rgb(255,255,255);}" )
			else:
				btn.setStyleSheet(
					" QPushButton {background-color:rgb(114,114,117);color:rgb(255,255,255);}")
			# 每次获取的都是最后一个btn
			# btn.clicked.connect(lambda : self.btnMyAction(btn,index))
			self.actionHandler(btn,index)
			if index == 16:
				bottomLayout.addWidget(btn,index/4,index%4,1,2)
			elif index<16:
				bottomLayout.addWidget(btn,index/4,index%4)
			else:
				bottomLayout.addWidget(btn,index/4,(index+1)%4)

			# print("key:",key)

	# 需要中转一下，否则每次传递的都是最后一个参数
	def actionHandler(self,btn,index):
		btn.clicked.connect(lambda: self.btnMyAction(btn, index))
	def btnMyAction(self,btn,index):
		print(btn.objectName())
		print("index : ",index)