#! /usr/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        hbox = QHBoxLayout(self)
        background = QPixmap("../ui/elements/background_small.png")
	nes = QPixmap("../ui/elements/nes.jpg")
        bg = QLabel(self)
	neslogo = QLabel(self)
        bg.setPixmap(background)
        neslogo.setPixmap(nes)
	neslogo.raise_()

        hbox.addWidget(bg)
        hbox.addWidget(neslogo)
        self.setLayout(hbox)
	#self.resize(1920, 1080)
        #self.move(10, 10)
        self.setWindowTitle('Dolos')
	#self.showFullScreen()
        self.show()        
        
        
    def control(self):
	if event == QtCore.Qt.Key_Escape:
            self.close()
        if event == QtCore.Qt.Key_Left:
            self.animFlag = False
            self.nextImage()
        if event == QtCore.Qt.Key_Right:
            self.animFlag = True
            self.nextImage()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
