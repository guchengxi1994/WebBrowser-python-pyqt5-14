'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-22 11:15:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-23 17:20:19
'''
import os
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,\
    QApplication,QAction,QRadioButton

from PyQt5.QtGui import QIcon,QPainter,QPen
from PyQt5.QtCore import QRect,Qt


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
        self.start_button.triggered.connect(self.start_game)

        self.pause_button = QAction(QIcon(BASE_DIR + '/static/time.png'),'Pause Quiz',self)
        self.main_toolbar.addAction(self.pause_button)


        #选项
        # self.rb1 = QRadioButton('Mode1--计时',self)
        # self.rb2 = QRadioButton('Mode2--倒计时',self)
        # self.rb3 = QRadioButton('Mode3--无计时',self)

        # self.rb1.move(50,100)
        # self.rb2.move(50,200)
        # self.rb3.move(50,300)
        

    
    def start_game(self):
        from utils.gameMode import MyDialog_GameMode_chosen

        dialog_gameType = MyDialog_GameMode_chosen()
        result = dialog_gameType.exec_()
        print(dialog_gameType.info1)


    # def paintEvent(self):
    #     # super().paintEvent(event)
    #     painter = QPainter()
    #     painter.begin(self)
    #     rect = QRect(20,20,500,200)
    #     painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
    #     painter.drawRect(rect)
    #     painter.end()
        # return super().paintEvent()


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())