#! /usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

window = QWidget()
window.move(300, 300)
window.setWindowTitle('Simple')
#window.showFullScreen() This works hard to close when done :)
window.show()
    
sys.exit(app.exec_())
