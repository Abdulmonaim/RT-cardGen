import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Start import Ui_MainWindow
from CardsSystem import Ui_VodafonEgypt
from ui_functions import*
#global Var
counter = 0
class MainWindow(QMainWindow):
	"""docstring for SplashScreen"""
	def __init__(self): 
		QMainWindow.__init__(self)
		self.ui = Ui_VodafonEgypt()
		self.ui.setupUi(self)
		self.ui.menubtn.clicked.connect(lambda:UIFunctions.toggleMenu(self,0,True))

class SplashScreen(QMainWindow):
	"""docstring for SplashScreen"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#Reomve the title bar
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint )
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		#shadow effect
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,0,0,60))
		self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

		#qTimer ==> start
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.progress)
		#timer in ms
		self.timer.start(20)
		#change disc
		#self.ui.label_disc.setText("<strong>Welcome</strong> to Vodafone Egypt")

		QtCore.QTimer.singleShot(1000,lambda:self.ui.label_loading.setText("Loading <strong>DataBase </strong> "))
		QtCore.QTimer.singleShot(1800,lambda:self.ui.label_loading.setText("Updating <strong> Cards Dates </strong>"))

		#show start
		self.show()

	def progress(self):
		global counter

		#set value to progress bar
		self.ui.progressBar.setValue(counter)

		# close splash scren and open app
		if counter > 100:
			# stop timer
			self.timer.stop()

			# show app
			self.main = MainWindow()
			self.main.show()

			#clsoe splash
			self.close()
		#increse counter
		counter += 1


if __name__== "__main__":
	app = QApplication(sys.argv)
	window = SplashScreen()
	sys.exit(app.exec_())
