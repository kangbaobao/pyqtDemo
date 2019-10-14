from PyQt5.QtWidgets import QWidget,QLabel
from PyQt5.QtGui import QPalette,QColor

class ImageWidget(QWidget):
	def __init__(self,p=None):
		super().__init__(p)
		self.setFixedSize(100, 100)
		print('ImageWidget...')


		self.imgLab = QLabel(self)
		self.imgLab.setGeometry(1,1,90,90)
		self.imgLab.setProperty('key','imglab')
		#注意一定要使用border-image,
		# 使用background-image就会出现窗口放大，背景图片过小重叠的现象
		self.imgLab.setStyleSheet('''
		  QLabel[key=imglab]{
		  	border-radius:45;
			border-image: url(./img1.jpeg);
				}
		''')
		self.backWidget = QWidget(self)
		self.backWidget.setGeometry(0,0,92,92)
		self.backWidget.setStyleSheet('''
		QWidget {
		border-radius:46;
		border:2px solid #cccccc;
		}
		QWidget:hover {
		border-radius:46;
		border:2px solid rgb(157,224,248);
		}
		''')

		self.pointWidget = QLabel(self)
		self.pointWidget.setGeometry((90-5)/2.0,90-2,10,10)
		# palette = QPalette()
		# palette.setColor(QPalette.Background, QColor().fromRgb(98, 227, 78))
		# self.pointWidget.setPalette(palette)
		self.pointWidget.setAutoFillBackground(True)
		self.pointWidget.setStyleSheet('''
		  QWidget{
			background-color:rgb(98,227,78);
			border-radius:5;
			}
		''')


