'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-22 11:15:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-28 09:12:11
'''
import os
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,\
    QApplication,QAction,QRadioButton,QLabel, \
    QLineEdit,QPushButton,QTextEdit,QInputDialog, \
    QWidget,QSizePolicy

from PyQt5.QtGui import QIcon,QPainter,QPen,QFont
from PyQt5.QtCore import QRect,Qt,QThread,QTimer
import numpy as np
from utils.extract2 import IdiomPinyinMeaning
import random
import datetime
from pypinyin import lazy_pinyin,pinyin
from utils.easyMode import iterator2list
from utils.userLog import UserLogWindow,UserInfo,UserChangeWindow
import pickle


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

        self.isActive = False  # 控件可用与否的判断

        # self.isLogged = False  # 登录与否的判断
        self.currentUser = None  # 当前用户的判断

        self.start_button = QAction(QIcon(BASE_DIR + '/static/test.png'),'Start Quiz',self)
        self.main_toolbar.addAction(self.start_button)
        self.start_button.triggered.connect(self.start_game)

        self.pause_button = QAction(QIcon(BASE_DIR + '/static/time.png'),'Pause Quiz',self)
        self.main_toolbar.addAction(self.pause_button)

        self.next_button = QAction(QIcon(BASE_DIR + '/static/next.png'),'Next Quiz',self)
        self.main_toolbar.addAction(self.next_button)
        self.next_button.triggered.connect(self.next_quiz)

        self.f5_button = QAction(QIcon(BASE_DIR + '/static/f5.png'),'Refresh',self)
        self.main_toolbar.addAction(self.f5_button)
        self.f5_button.triggered.connect(self.f5)

        #用户
        self.user_button = QAction(QIcon(BASE_DIR + '/static/user.png'),'User Info',self)
        

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.main_toolbar.addWidget(spacer)
        self.main_toolbar.addAction(self.user_button)

        self.user_button.triggered.connect(self.logIN)




        self.timeRecord = QLabel('',self)
        self.timeRecord.move(325,100)
        self.timeRecord.setFixedWidth(500)

        self.gameModeChosen = ''

        self.idioms = []
        self.thisQuiz = IdiomPinyinMeaning("","","","","")
        

        self.totalNumNumber = 0
        self.totalNum = QLabel('总数： '+str(self.totalNumNumber),self)
        self.totalNum.move(575,100) 


        self.correctNumNumber = 0
        self.correctNum = QLabel('准确数量： '+str(self.correctNumNumber),self)
        self.correctNum.move(575,200) 
        


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




        self.resultLabel = QLabel('回答：',self)
        self.resultLabel.move(100,400)

        # self.resultEdit.setReadOnly(True)
        self.resultEdit = QLineEdit(self)
        self.resultEdit.setText("")
        self.resultEdit.move(150,400)
        self.resultEdit.returnPressed.connect(self.tijiao)

        self.resultButton = QPushButton(self)
        self.resultButton.move(250,400)
        self.resultButton.setFixedSize(31,31)
        self.resultButton.setStyleSheet("QPushButton{border-image: url(./static/tijiao.png)}")
        self.resultButton.clicked.connect(self.tijiao)
        self.resultButton.setToolTip("Next")




        self.quizMeaningText = QTextEdit(self)
        self.quizMeaningText.move(100,275)
        self.quizMeaningText.setFixedWidth(150)
        self.quizMeaningText.setReadOnly(True)

        self.showLoading()
        self.readTxt()

        self.timer = QTimer()
        self.step = 0

        self.initUser()

    def initUser(self):
        from utils.userLog import loadUsers
        userFilePath = BASE_DIR+os.sep+"static"+os.sep+"userInfo.pkl"
        g = loadUsers(userFilePath)
        s = filter(lambda x:x.isCurrentUser == True,g )
        tmp = iterator2list(s)
        if len(tmp)>0:
            self.currentUser = tmp[0]
        else:
            self.currentUser = UserInfo("","",0,"",False,False)
        
        

    def logIN(self):
        if self.currentUser is not None:
            # pass
            user = UserChangeWindow(self.currentUser.username)
            result = user.exec_()
            switch = user.switch
            print(switch)
        else:
            user = UserLogWindow()
            result = user.exec_()

            self.currentUser = user.currentUser
            print(self.currentUser)

    
    def tijiao(self):

        self.isActive = True
        self.next_button.setEnabled(False)

        quiz = self.quizEdit.text()
        res = self.resultEdit.text()
        # print(res)
        self.resultEdit.setText("")
        quiz_list = lazy_pinyin(quiz.strip())
        res_list = lazy_pinyin(res.strip())
        self.totalNumNumber += 1
        

        # print(quiz_list)
        # print(res_list)
        if res.strip()!= "":
            if quiz_list[-1] == res_list[0]:
                
                s = filter(lambda x:x.idiom.strip() == res.strip(),self.idioms)
                
                if len(list(s))>0:
                    # print(True)
                    self.correctNumNumber += 1
                    self.next_quiz_end(res_list[-1])
                else:
                    self.next_quiz()
            else:
                self.next_quiz()
        else:
            self.next_quiz()

        self.totalNum.setText('总数： '+str(self.totalNumNumber))
        self.correctNum.setText('准确数量： '+str(self.correctNumNumber))


    def f5(self):
        """
        刷新
        """
        self.next_quiz()
        self.isActive = False
        self.next_button.setEnabled(True)
        self.totalNumNumber = 0
        self.correctNumNumber = 0
        self.totalNum.setText('总数： '+str(self.totalNumNumber))
        self.correctNum.setText('准确数量： '+str(self.correctNumNumber))

    def freeze(self):
        """
        禁用所有控件
        """
        pass



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

    def next_quiz_end(self,end:str):
        # pass
        s = filter(lambda x:x.start.strip() == end.strip(),self.idioms)

        res = iterator2list(s)

        if len(res)>0:

            ind = random.randint(0,len(res)-1)
            self.thisQuiz = res[ind]
            self.quizEdit.setText(res[ind].idiom)
            # print(self.idioms[0])
            self.pinyinLabel.setText('拼音：'+res[ind].pinyin)
            self.quizMeaningText.setText("")
        else:
            self.next_quiz()
      

    def readTxt(self):
        # pass
        self.idioms = np.load(idiomPath,allow_pickle=True)
        self.next_quiz()
        # self.thisQuiz = self.idioms[0]
        # self.quizEdit.setText(self.thisQuiz.idiom)
        # # print(self.idioms[0])
        # self.pinyinLabel.setText('拼音：'+self.thisQuiz.pinyin)
        
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

        self.isActive = True
        self.next_button.setEnabled(False)

        dialog_gameType = MyDialog_GameMode_chosen()
        result = dialog_gameType.exec_()
        # print(dialog_gameType.info1)
        if dialog_gameType.info1.startswith("Mode1"):
            self.gameModeChosen = "Mode1"
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
            self.gameModeChosen = "Mode2"
            text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入时间：')
            if ok:
                if "" == text or text is None:
                    pass
                else:
                    # from utils.strISnumber import is_number 
                    i = -1                
                    if text.isdigit():
                        # import unicodedata
                        i = int(text)
                        
                    self.timeRecord.setText("Remaining Time: "+str(i))
                        
            self.timeRecord.setVisible(True)
            # pass
        else:
            self.timeRecord.setVisible(False)
            # pass
            self.gameModeChosen = "Mode3"



        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())