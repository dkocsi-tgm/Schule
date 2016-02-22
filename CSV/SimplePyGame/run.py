__author__ = 'Daniel'
from PySide import QtCore, QtGui
import sys
from CSV.SimplePyGame.mainWindow_ui import Ui_MainWindow

app=QtGui.QApplication(sys.argv)
ui=Ui_MainWindow()
ui.show()
sys.exit(app.exec_())