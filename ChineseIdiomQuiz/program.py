'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-22 11:15:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-22 11:34:27
'''
import os
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,\
    QApplication,QAction

from PyQt5.QtGui import QIcon

BASE_DIR = os.path.abspath(os.curdir)

idiomPath = BASE_DIR + "/static/words.txt"

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()   
        self.setWindowTitle("Idiom Quiz")
        self.resize(800,600)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + '/static/icon.png'))
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(self.main_toolbar)

        self.start_button = QAction(QIcon(BASE_DIR + '/static/test.png'),'Start Quiz',self)
        self.main_toolbar.addAction(self.start_button)

        self.pause_button = QAction(QIcon(BASE_DIR + '/static/time.png'),'Pause Quiz',self)
        self.main_toolbar.addAction(self.pause_button)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())