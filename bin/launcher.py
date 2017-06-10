#! /usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLayout, QGridLayout
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap
import subprocess


class dolos(QWidget):
	def __init__(self):
		super(dolos, self).__init__()
		self.window()

	def window(self):
		self.setWindowTitle('Dolos')
		self.setAttribute(Qt.WA_StyledBackground)
		self.setStyleSheet("background-image: url(/home/atlas/dev/dolos/ui/elements/background.png); border: none")
		self.showFullScreen()
		self.setFocus
		
		nes = QLabel()
		nesimage = QPixmap("/home/atlas/dev/dolos/ui/elements/nes.png")
		nes.setPixmap(nesimage)
		
		snes = QLabel()
		snes.setPixmap(QPixmap("/home/atlas/dev/dolos/ui/elements/snes.png"))
		mame = QLabel()
		mame.setPixmap(QPixmap("/home/atlas/dev/dolos/ui/elements/mame.png"))
		indie = QLabel()
		indie.setPixmap(QPixmap("/home/atlas/dev/dolos/ui/elements/indie.png"))
		layout = QGridLayout()
		#layout = QHBoxLayout()
		#layout.setSpacing(200)
		layout.addWidget(nes, 2, 1)
		layout.addWidget(mame, 2, 2)
		layout.addWidget(snes, 2, 3)
		layout.addWidget(indie, 2, 4)
		self.setLayout(layout)
		#self.show()

	def keyPressEvent(self, event):
		#print(event)
		if event.key() == Qt.Key_Escape:
			print('User called quit')
			self.close()
		elif event.key() == Qt.Key_Left:
			print('Left')
		elif event.key() == Qt.Key_Right:
			print('Right')
		elif event.key() == Qt.Key_A:
			args = ("/opt/pycharm-community-2017.1.3/bin/pycharm.sh")
			subprocess.Popen(args)
			print('launched'+args)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = dolos()
	sys.exit(app.exec_())
