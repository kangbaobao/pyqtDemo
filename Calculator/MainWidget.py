from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QHBoxLayout,QGridLayout,QPushButton,QMessageBox
from  PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette,QColor,QFont
from  PyQt5.Qt import Qt

class MianWiget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent);
		self.setFixedSize(QSize(250,330))
		self.setWindowTitle('计算器')
        #阻止窗口最大最小化
        # w.setWindowFlag(~Qt.WindowMinimizeButtonHint)#and ~ Qt.WindowMinimizeButtonHint Qt.WindowMaximizeButtonHint
        # PyQT禁止调整窗口大小：
        #w.setFixedSize(w.width(),w.height())
		palette = QPalette()
		palette.setColor(QPalette.Background,QColor().fromRgb(68,69,73))
		self.setPalette(palette)
		self.strList = ['AC','+/-','%','/',
						'7', '8', '9', '*',
						'4', '5', '6', '-',
						'1', '2', '3', '+',
						'0', '.', '=',
						];
		self.setupUI()
		#计算处理
		self.stackList = [];

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
		if index == 0:
			# 清空数据处理
			self.stackList.clear()
			self.showLab.setText('0')
		elif index ==18:
			try:
				# 计算处理
				s = ''.join(self.stackList)
				print('s : ',s)
				value = eval(s)
				print('value:',value )
				self.stackList.clear()
				self.stackList.append(str(value))
				self.showLab.setText(str(value))
			except Exception as e :
			# 发生异常，执行这块代码
				repay = QMessageBox.warning(self,'title',str(e),QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
				print("repay : ",repay==QMessageBox.No);
		elif index ==1:
		 # 正负号处理 从stackList中获取最后一个数字
			self.fuhaohandler()
			# pass
		else:
			#数值和符号
			if self.is_number(btn.text()):
				if len(self.stackList)>0:
					if self.is_number(self.stackList[len(self.stackList)-1]):
						last = self.stackList.pop()
						print("last : ", last)

						self.stackList.append(''+last+btn.text())
					else:
						self.stackList.append(btn.text())
				else:
					self.stackList.append(btn.text())
			else:
				self.stackList.append(btn.text())
			print("stackList : ",self.stackList)
			s = ''.join(self.stackList)
			self.showLab.setText(s)

	# 教程代码当出现多个汉字数字时会报错，通过遍历字符串解决
	# 对汉字表示的数字也可分辨
	def is_number(self,s):
		try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
			float(s)
			return True
		except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
			pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
		# try:
		# 	import unicodedata  # 处理ASCii码的包
		# 	for i in s:
		# 		unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
		# 	# return True
		# 	return True
		# except (TypeError, ValueError):
		# 	pass
		return False
	# 正负号处理
	def fuhaohandler(self):
		if len(self.stackList) > 0:
			# 列表逆向
			# newList = self.stackList.copy();
			# newList.reverse()
			self.stackList.reverse()
			for index, value in enumerate(self.stackList):
				if self.is_number(value):
					# 正数取负数，负数变正数
					newVlaue = float(value)
					if newVlaue > 0:
						# self.stackList.pop(len(newList)-index-1)
						# self.stackList.insert(len(newList)-index-1,'-%0.0f' % newVlaue)
						self.stackList.pop(index)
						self.stackList.insert(index,'-%0.0f' % newVlaue)
						break;
					elif newVlaue == 0:
						break;
					else:
						# self.stackList.pop(len(newList)-index-1)
						# self.stackList.insert(len(newList)-index-1,str(abs(newVlaue)))
						self.stackList.pop(index )
						self.stackList.insert(index, str(abs(newVlaue)))
						break;
			self.stackList.reverse()
			print("self.stackList : ",self.stackList)
			s = ''.join(self.stackList)
			self.showLab.setText(s)
