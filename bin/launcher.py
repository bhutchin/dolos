#! /usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class dolos(QWidget):

    def __init__(self):
		super(dolos, self).__init__()
		self.window()

    def window(self):
        #window = QWidget()
        self.setWindowTitle('Dolos')
        self.setStyleSheet("background-image: url(../ui/elements/background.png); border: none")
        self.showFullScreen()
        #window.show()
    
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = dolos()
	sys.exit(app.exec_())
