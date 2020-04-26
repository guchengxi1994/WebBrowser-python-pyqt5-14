'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-22 11:15:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-26 09:17:28
'''
import os
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,\
    QApplication,QAction,QRadioButton,QLabel, \
    QLineEdit,QPushButton,QTextEdit

from PyQt5.QtGui import QIcon,QPainter,QPen,QFont
from PyQt5.QtCore import QRect,Qt,QThread,QTimer
import numpy as np
from utils.extract2 import IdiomPinyinMeaning
import random
import datetime


BASE_DIR = os.path.abspath(os.curdir)

idiomPath = BASE_DIR + "/static/idioms.npy"



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

        self.next_button = QAction(QIcon(BASE_DIR + '/static/next.png'),'Next Quiz',self)
        self.main_toolbar.addAction(self.next_button)
        self.next_button.triggered.connect(self.next_quiz)

        self.timeRecord = QLabel('',self)
        self.timeRecord.move(325,100)
        self.timeRecord.setFixedWidth(500)

        self.idioms = []
        self.thisQuiz = IdiomPinyinMeaning("","","")

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
        self.pinyinLabel = QLabel('拼音：',self)


        self.quizLabel.move(100,200)
        self.pinyinLabel.move(100,235)
        self.pinyinLabel.setFixedWidth(200)

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
        self.quizMeaningText.move(100,275)
        self.quizMeaningText.setFixedWidth(150)
        self.quizMeaningText.setReadOnly(True)

        self.showLoading()
        self.readTxt()

        self.timer = QTimer()
        self.step = 0





    def showLoading(self):
        from utils.loading import ProBar
        pb = ProBar()
        pb.raise_()
        pb.exec_()

    def next_quiz(self):
        ind = random.randint(0,len(self.idioms)-1)
        self.thisQuiz = self.idioms[ind]
        self.quizEdit.setText(self.thisQuiz.idiom)
        # print(self.idioms[0])
        self.pinyinLabel.setText('拼音：'+self.thisQuiz.pinyin)
        self.quizMeaningText.setText("")

    def readTxt(self):
        # pass
        self.idioms = np.load(idiomPath,allow_pickle=True)
        self.thisQuiz = self.idioms[0]
        self.quizEdit.setText(self.thisQuiz.idiom)
        # print(self.idioms[0])
        self.pinyinLabel.setText('拼音：'+self.thisQuiz.pinyin)
        
    def showMeaning(self):
        # print(self.quizMeaningText.toPlainText())
        if len(self.quizMeaningText.toPlainText()) < 5:
            self.quizMeaningText.setText(self.thisQuiz.meaning)
        else:
            self.quizMeaningText.setText("")

    def startRecordTime(self):
        # self.timer.start(1000)
        self.step += 1
        
        self.timeRecord.setText("Cost Time: "+str(datetime.timedelta(seconds=self.step)))
    
    def start_game(self):
        from utils.gameMode import MyDialog_GameMode_chosen
        from utils.backtime import BackTime

        dialog_gameType = MyDialog_GameMode_chosen()
        result = dialog_gameType.exec_()
        # print(dialog_gameType.info1)
        if dialog_gameType.info1.startswith("Mode1"):
            # pass
            bt = BackTime()
            bt.raise_()
            bt.exec_()
            self.timeRecord.setVisible(True)
            self.timer.start(1000)
            self.timer.timeout.connect(self.startRecordTime)
            # if self.timer.isActive():                
            #     self.start_game()

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