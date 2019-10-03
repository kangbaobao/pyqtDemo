from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QLineEdit,QAction
from PyQt5.QtGui import QPalette,QColor,QFont,QPixmap,QBrush,QIntValidator,QDoubleValidator,QRegExpValidator,QIcon
from PyQt5.QtCore import QRect,QRegExp,QMargins
from PyQt5.Qt import Qt
import sys
# QLabel
def createLab(p):
	lab = QLabel()
	lab.setText('''我希望遇见一个如你一般的人,如山间清爽的风,如古城温暖的光,从清晨到夜晚,由山野到书房,只是这最后是你,就好''')
	lab.setParent(p)
	lab.setGeometry(QRect(20, 40, 400,200))
	# 创建调色板
	p = QPalette()
	# 设置背景色
	p.setColor(QPalette.Background, QColor.fromRgb(255, 0, 0))
	# 设置前景色
	p.setColor(QPalette.WindowText, Qt.white)
	#QPalette设置背景图片
	pixmap =  QPixmap('./image/img1.jpeg')
	pixmap.scaled(lab.width(),lab.height(),Qt.KeepAspectRatio)
	# p.setBrush(QPalette.Background, QBrush(pixmap));#lab.backgroundRole()
	lab.setPalette(p)
	# 在设置对话框和控件的背景色时还会用到
	lab.setAutoFillBackground(True)
	# 设置字体 Mac下字体库路径 /System/Library/Fonts /Library/Fonts win 路径 C:\Windows\Fonts
	font = QFont()
	font.setFamily("华文宋体")#华文宋体 'GB18030 Bitmap'
	'''
	//font.setFamily("微软雅黑");//字体
	//font.setPixelSize(25);//文字像素大小
	//font.setPointSize(20);//文字大小
	//font.setUnderline(true);//下划线
	//font.setStrikeOut(true);//中划线
	//font.setOverline(true);//上划线
	//font.setItalic(true);//斜体
	//font.setBold(true);//粗体
	// font.setCapitalization(QFont.Capitalize);//首字母大写
	// font.setLetterSpacing(QFont.PercentageSpacing,200);//间距
	'''
	#设置字体大小
	font.setPointSize(20)
	# 间距
	# font.setLetterSpacing(QFont.PercentageSpacing, 200)
	lab.setFont(font)

	# 自动换行
	lab.setWordWrap(True)
	# 对齐方式
	# Qt.AlignJustify使每行排齐
	lab.setAlignment(Qt.AlignTop|Qt.AlignJustify)
	# # 设置图片
	# lab.setPixmap(QPixmap('./image/img1.jpeg'))
	# # 当照片大小和QLabel大小不适应时，可以设置
	# lab.setScaledContents(True);  # 这样照片会自动适应大小
	# return lab


#QLineEdit
def lineEditTest(p):
	line = QLineEdit(p)
	line.move(20,40)
	line.resize(200,30)
	# 设置默认提示文字
	line.setPlaceholderText("请输入用户名")
	#设置输入文字
	# line.setText("用户名")
	# 设置为只读，不可编辑
	# line.setReadOnly(True)
	# 最大输入字符
	line.setMaxLength(10)
	# 设置文本验证规则
	# # 整型验证器
	# intV = QIntValidator()
	# # 只能输入1～99
	# intV.setRange(1,99)
	# line.setValidator(intV)

	# 	浮点数验证器
	# douV  = QDoubleValidator()
	# douV.setRange(-360,360)
	# # 记数法
	# douV.setNotation(QDoubleValidator.StandardNotation)
	# # 小数的位数
	# douV.setDecimals(3)
	# line.setValidator(douV)

	# 正则表达式验证器
	reg = QRegExp('[a-zA-z]+')
	regV = QRegExpValidator(reg)
	line.setValidator(regV)
	# 显示密码
	line.setEchoMode(QLineEdit.Password)
	#设置文字外边距 QMargins(int left,int top, int right, int bottom)
	line.setTextMargins(QMargins(20,5,5,5))
if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()

	# createLab(w)
	lineEditTest(w)
	w.show()
	sys.exit(app.exec_())
