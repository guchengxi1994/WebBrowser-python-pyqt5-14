'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-22 11:15:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-24 10:25:39
'''
import os
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,\
    QApplication,QAction,QRadioButton,QLabel, \
    QLineEdit,QPushButton,QTextEdit

from PyQt5.QtGui import QIcon,QPainter,QPen,QFont
from PyQt5.QtCore import QRect,Qt,QThread


BASE_DIR = os.path.abspath(os.curdir)

idiomPath = BASE_DIR + "/static/words.txt"


class MyThread(QThread):
    def __init__(self):
        super(MyThread,self).__init__()

    def run(self):
        from utils.loading import ProBar
        pb = ProBar()
        pb.raise_()
        pb.exec_()




class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()   
        self.setWindowTitle("Idiom Quiz")
        self.resize(800,600)
        self.setFixedSize(800,600)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + '/static/icon.png'))
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(self.main_toolbar)

        self.start_button = QAction(QIcon(BASE_DIR + '/static/test.png'),'Start Quiz',self)
        self.main_toolbar.addAction(self.start_button)
        self.start_button.triggered.connect(self.start_game)

        self.pause_button = QAction(QIcon(BASE_DIR + '/static/time.png'),'Pause Quiz',self)
        self.main_toolbar.addAction(self.pause_button)

        self.timeRecord = QLabel('0',self)
        self.timeRecord.move(385,100)

        font1 = QtGui.QFont() 
        #字体
        font1.setFamily('微软雅黑')
        #加粗
        font1.setBold(True) 
        #大小
        font1.setPointSize(13) 
        font1.setWeight(75) 
        # self.label.setFont(font) 
        self.timeRecord.setFont(font1)
        self.timeRecord.setVisible(False)
        # self.timeRecord.setStyleSheet("color:rgb(20,20,20,255);font-size:16px;font-weight:bold:text")
        # self.timeRecord.isVisible(False)

        self.quizLabel = QLabel('出题：',self)

        self.mt = MyThread()

        self.quizLabel.move(100,200)
        self.quizEdit = QLineEdit(self)
        self.quizEdit.move(150,200)
        self.quizEdit.setReadOnly(True)
        self.quizEdit.setText("test")

        self.quizShowMeaningButton = QPushButton(self)
        self.quizShowMeaningButton.move(238,190)
        self.quizShowMeaningButton.setFixedSize(50,50)
        self.quizShowMeaningButton.setStyleSheet("QPushButton{border-image: url(./static/meaning.png)}")
        self.quizShowMeaningButton.clicked.connect(self.showMeaning)
        self.quizShowMeaningButton.setToolTip("Show Idiom Meaning")


        self.quizMeaningText = QTextEdit(self)
        self.quizMeaningText.move(100,235)
        self.quizMeaningText.setFixedWidth(150)
        self.quizMeaningText.setReadOnly(True)

        self.showLoading()
        # self.quizEdit.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        # self.quizEditAction = QAction(self)
        # self.quizEditAction.setIcon(QIcon("/static/meaning.png"))
        # self.quizEditAction.triggered.connect(self.showMeaning)
        

        # self.quizEdit.addAction(quizEditAction,QLineEdit.TrailingPosition)

        


        #选项
        # self.rb1 = QRadioButton('Mode1--计时',self)
        # self.rb2 = QRadioButton('Mode2--倒计时',self)
        # self.rb3 = QRadioButton('Mode3--无计时',self)

        # self.rb1.move(50,100)
        # self.rb2.move(50,200)
        # self.rb3.move(50,300)

    def showLoading(self):
        self.mt.start()
        # mt = MyThread()
        # mt.run()

    def readTxt(self):
        pass
        
    def showMeaning(self):
        # print("aaaaaa")
        print("aaaaa")
    
    def start_game(self):
        from utils.gameMode import MyDialog_GameMode_chosen

        dialog_gameType = MyDialog_GameMode_chosen()
        result = dialog_gameType.exec_()
        # print(dialog_gameType.info1)
        if dialog_gameType.info1.startswith("Mode1"):
            # pass
            self.timeRecord.setVisible(True)
        elif dialog_gameType.info1.startswith("Mode2"):
            self.timeRecord.setVisible(True)
            # pass
        else:
            self.timeRecord.setVisible(False)
            pass


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