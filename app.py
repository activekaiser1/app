import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
 
 
 
app = QApplication(sys.argv)
 
web = QWebEngineView()
 
web.load(QUrl("https://wavesurfer-js.org/"))
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
web.setWindowFlags(flags)
web.show()
 
 
sys.exit(app.exec_())