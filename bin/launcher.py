#! /usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

window = QWidget()
window.move(300, 300)
window.setWindowTitle('Simple')
window.setStyleSheet("background-image: url(../ui/elements/background_small.png); border: none")
window.showFullScreen()
#window.show()
    
sys.exit(app.exec_())
