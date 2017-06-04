#! /usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


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
		nes.setPixmap(QPixmap("/home/atlas/dev/dolos/ui/elements/nes.jpg"))
		snes = QLabel()
		snes.setPixmap(QPixmap("/home/atlas/dev/dolos/ui/elements/snes.jpg"))
		hbox = QHBoxLayout()
		hbox.addWidget(nes)
		hbox.addWidget(snes)
		self.setLayout(hbox)
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
			print('Select')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = dolos()
	sys.exit(app.exec_())
