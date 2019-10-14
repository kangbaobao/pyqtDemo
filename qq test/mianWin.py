from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QHBoxLayout,\
	QLineEdit,QPushButton,QGridLayout,QRadioButton,QButtonGroup
from PyQt5.QtGui import QPixmap,QRegExpValidator,QIcon,QDesktopServices
from PyQt5.QtCore import QMargins,QRegExp,QUrl
from PyQt5.Qt import Qt
from ImageWidget import ImageWidget
class MainWidget(QWidget):
	def __init__(self,p=None):
		super().__init__(p)
		# self.setFixedSize(240,320)
		self.setFixedWidth(240)
		self.setFixedHeight(260)
		self.setWindowTitle("QQ")
		self.initUI()
		self.setStyleSheet('''
		QLineEdit {
			border:none;
			background:transparent;
			border-bottom:1px solid #999999;
		}
		QAbstractButton {
			border:none;
			font-size:12pt
		}
		''')
	# 				border-style:outset	;
	def initUI(self):
		mainLayout= QVBoxLayout()

		mainLayout.setContentsMargins(0,0,0,0)

		self.setLayout(mainLayout)

		topLayout = QHBoxLayout()
		topLayout.setContentsMargins(0,24,0,0)
		mainLayout.addLayout(topLayout)
		self.imgLab = ImageWidget()#QLabel()

		# pixmap = QPixmap('./img1.jpeg')
		# self.imgLab.setPixmap(pixmap)
		# self.imgLab.setScaledContents(True)
		topLayout.addWidget(self.imgLab,Qt.AlignCenter)
		# self.imgLab.setFixedSize(80,80)
		# self.imgLab.setProperty('key','imglab')
		# #注意一定要使用border-image,
		# # 使用background-image就会出现窗口放大，背景图片过小重叠的现象
		# self.imgLab.setStyleSheet('''
		#   QLabel[key=imglab]{
		#   	border-radius:40;
		# 	border-image: url(./img1.jpeg);
		# 		}
		# ''')
		inputLayout = QVBoxLayout()
		mainLayout.addLayout(inputLayout)
		userNameEdit = QLineEdit()
		userNameEdit.setPlaceholderText("输入用户名")
		userNameEdit.setFixedHeight(25)
		# userNameEdit.setFrame(False)
		# userNameEdit.setStyleSheet('''
		# QLineEdit {
		# 	background:transparent;
		# 	border-style:outset	;
		# 	border-bottom:1px solid #999999;
		# }
		# ''')
		inputLayout.addWidget(userNameEdit)
		userNameEdit.setMaxLength(12)
		reg = QRegExp('[0-9]+')
		userV = QRegExpValidator(reg)
		userNameEdit.setValidator(userV)
		inputLayout.setContentsMargins(20,0,20,0)

		inputInnerLayout = QHBoxLayout()
		inputLayout.addLayout(inputInnerLayout)
		passwordEdit = QLineEdit()
		passwordEdit.setPlaceholderText('输入密码')
		passwordEdit.setEchoMode(QLineEdit.Password)
		passwordEdit.setFixedHeight(userNameEdit.height())
		inputInnerLayout.addWidget(passwordEdit)
		loginBtn = QPushButton()
		loginBtn.setIcon(QIcon('./add.png'))
		loginBtn.setFixedSize(30,30)
		inputInnerLayout.addWidget(loginBtn)

		jianTouLayout = QHBoxLayout()
		# jianTouLayout.setContentsMargins(0,20,0,0)
		mainLayout.addLayout(jianTouLayout)
		jiantouBtn = QPushButton()
		jianTouLayout.addWidget(jiantouBtn)
		jiantouBtn.setText('下箭头')
		jiantouBtn.setFixedSize(80,30)
		jiantouBtn.setCheckable(True)
		jiantouBtn.toggled.connect(lambda :self.jianTouAction(jiantouBtn))

		self.bottomLayout =  QGridLayout()
		self.bottomLayout.setContentsMargins(10,0,10,0)
		self.createBottomView()
		mainLayout.addLayout(self.bottomLayout)

		# mainLayout.addStretch(1)
	def createBottomView(self):
		rememberPsdBtn = QRadioButton()
		rememberPsdBtn.setText('记住密码')
		rememberPsdBtn.hide()

		autoLoginBtn = QRadioButton()
		autoLoginBtn.setText('自动登录')
		autoLoginBtn.hide()

		gourp = QButtonGroup(rememberPsdBtn)
		gourp.addButton(rememberPsdBtn)
		gourp.addButton(autoLoginBtn)
		gourp.setExclusive(False)

		forgetPsdBtn = QPushButton()
		forgetPsdBtn.setText('忘记密码')
		forgetPsdBtn.clicked.connect(lambda :self.btnAction(forgetPsdBtn))
		forgetPsdBtn.hide()

		registeredBtn = QPushButton()
		registeredBtn.setText('注册账号')
		registeredBtn.hide()
		self.bottomLayout.addWidget(rememberPsdBtn,1,1)
		self.bottomLayout.addWidget(forgetPsdBtn,1,2)
		self.bottomLayout.addWidget(autoLoginBtn, 2, 1)
		self.bottomLayout.addWidget(registeredBtn, 2, 2)
	def btnAction(self,btn):
		if btn.text() =='忘记密码':
			# 跳转到网页
			QDesktopServices.openUrl(QUrl('http:://www.baidu.com'))
	def jianTouAction(self,btn):
		print('btn:',btn.isChecked(),self.bottomLayout.itemAt(0))
		if btn.isChecked() :
			self.setFixedHeight(320)
			for i in range(self.bottomLayout.count()):
				self.bottomLayout.itemAt(i).widget().show()
		else:
			self.setFixedHeight(260)
			for i in range(self.bottomLayout.count()):
				self.bottomLayout.itemAt(i).widget().hide()
