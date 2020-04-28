'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 16:54:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-28 08:59:06
'''

from PyQt5.QtCore import Qt, QTimer,QRect
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit, \
    QMessageBox
import sys,os
import pickle
from pypinyin import pinyin
from PyQt5.QtGui import QImage,QPixmap
# import cv2

BASE_DIR = os.path.abspath(os.curdir)
# parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), "..")) #for test
parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
userInfoFilePath = parent_Base_dir + os.sep + "static" + os.sep + "userInfo.pkl"


class UserInfo(object):
    def __init__(self,username,password,userlevel,email,isLogged=True,isCurrentUser=True):
        self.username = username
        self.password = password
        self.userlevel = userlevel
        self.email = email
        self.isLogged = isLogged
        self.isCurrentUser = isCurrentUser
    
    def __eq__(self,other):
        if not isinstance(other,self.__class__):
            return False
        else:
            return self.username == other.username
    
    def __str__(self):
        return self.username

    def __hash__(self):
        return hash(self.username) + hash(self.password) + hash(self.userlevel) + hash(self.email)
        


def initAdmin(userInfoFilePath):
    if os.path.exists(userInfoFilePath):
        pass
    else:
        userList = []
        userSet = set()

        u = UserInfo("admin",'admin',5,"admin@test.com",False,False)
        userSet.add(u)
        userList = list(userSet)

        pk_file = open(userInfoFilePath,'wb')
        pickle.dump(userList,pk_file)
        pk_file.close()
        

def loadUsers(userInfoFilePath):
    # print(userInfoFilePath)
    pk_file = open(userInfoFilePath,'rb')
    g = pickle.load(pk_file)
    pk_file.close()

    return g

def userAddU(userInfoFilePath,u:UserInfo):
    g = loadUsers(userInfoFilePath)
    for i in g:
        i.isLogged == False
        i.isCurrentUser == False
    setG = set(g)
    setG.add(u)

    pk_file = open(userInfoFilePath,'wb')
    pickle.dump(list(setG),pk_file)
    pk_file.close()

    


def iterator2list(itera):
    res = []
    for i in itera:
        res.append(i)
    return res

class UserLogWindow(QDialog):
    def __init__(self):
        super(UserLogWindow,self).__init__()

        initAdmin(userInfoFilePath)

        self.setFixedSize(300,200)

        self.userNameLable = QLabel("用户名：",self)
        self.userNameEdit = QLineEdit(self)

        self.passwordLable = QLabel("密码：",self)
        self.passwordEdit = QLineEdit(self)

        self.emailLable = QLabel("E-mail：",self)
        self.emailEdit = QLineEdit(self)
        
        self.logButton = QPushButton(self)
        self.logButton.setText("登录")

        self.newButton = QPushButton(self)
        self.newButton.setText("注册")

        self.userNameLable.move(20,20)
        self.userNameEdit.move(100,20)

        self.passwordLable.move(20,60)
        self.passwordEdit.move(100,60)

        self.emailLable.move(20,100)
        self.emailEdit.move(100,100)

        self.logButton.move(60,150)
        self.newButton.move(160,150)

        self.logButton.clicked.connect(self.logIn)
        self.newButton.clicked.connect(self.createUser)

        self.currentUser = None

    
    def logIn(self):
        if self.userNameEdit.text().strip() == "" or self.passwordEdit.text().strip() == "":
            QMessageBox.warning(self,'警告','用户名或者密码为空',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        else:
            g = loadUsers(userInfoFilePath)

            s = filter(lambda x:x.username == self.userNameEdit.text() and x.password == self.passwordEdit.text().strip(),g )

            tmp = iterator2list(s)

            if len(tmp)>0:               
                self.currentUser = tmp[0] 
                userAddU(userInfoFilePath,self.currentUser) 
                self.close()           
                # print(self.currentUser)
            else:
                QMessageBox.warning(self,'警告','用户名或者密码错误',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

    
    def createUser(self):
        if self.userNameEdit.text().strip() == "" or self.passwordEdit.text().strip() == "" or self.emailEdit.text().strip()=="":
            QMessageBox.warning(self,'警告','用户名或者密码或者邮箱为空',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        else:
            g = loadUsers(userInfoFilePath)
            s = filter(lambda x:x.username == self.userNameEdit.text(),g )
            tmp = iterator2list(s)
            if len(tmp)>0:
                QMessageBox.warning(self,'警告','用户名重复',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            else:
                u = UserInfo(self.userNameEdit.text().strip(),self.passwordEdit.text().strip(),1,self.emailEdit.text().strip())
                self.currentUser = u

                userAddU(userInfoFilePath,u)
                self.close()
    

    @staticmethod
    def getCurrentUser(parent=None):
        dialog = UserLogWindow(parent)
        result = dialog.exec_()
        return dialog.currentUser




class UserChangeWindow(QDialog):
    def __init__(self,userName="admin"):
        super(UserChangeWindow,self).__init__()
        self.setFixedSize(300,200)
        self.thisUser = userName

        self.userNameLable = QLabel("用户名：",self)
        self.userNameEdit = QLineEdit(self)
        self.userNameEdit.setEnabled(False)
        self.userNameEdit.setText(userName)

        self.statusLable = QLabel("状态:",self)
        # self.passwordEdit = QLineEdit(self)

        self.logButton = QPushButton(self)
        self.logButton.setText("切换用户")

        self.newButton = QPushButton(self)
        self.newButton.setText("退出")

        self.userNameLable.move(20,20)
        self.userNameEdit.move(100,20)

        self.statusLable.move(20,60)
        # self.passwordEdit.move(100,60)

        self.logButton.move(60,150)
        self.newButton.move(160,150)
        self.switch = 0

        self.logButton.clicked.connect(self.switchUser)
        self.newButton.clicked.connect(self._exit_)


        # pix = QPixmap(parent_Base_dir+os.sep+"static"+os.sep+"medal.png")
        self.ImageView = QLabel(self)
        self.ImageView.setGeometry(QRect(20, 20, 20, 20))
        self.ImageView.setText("")
        self.ImageView.setObjectName("ImageView")
        self.ImageView.setScaledContents(True)
        # self.ImageView.setPixmap(pix)

        self.ImageView.move(100,60)
        self.ImageView.setToolTip("User Info")
        self.initInfo()



        

    
    def initInfo(self):
        # parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        userInfoFilePath = parent_Base_dir + os.sep + "static" + os.sep + "userInfo.pkl"
        g = loadUsers(userInfoFilePath)
        s = filter(lambda x:x.username == self.thisUser,g )
        tmp = iterator2list(s)

        if tmp[0].userlevel == 5:
            pix = QPixmap(parent_Base_dir+os.sep+"static"+os.sep+"top_level.png")
            
        else:
            pix = QPixmap(parent_Base_dir+os.sep+"static"+os.sep+"medal.png")
        self.ImageView.setPixmap(pix)

    
    def switchUser(self):
        self.switch = 1
        self.close()
    
    def _exit_(self):
        self.close()

    @staticmethod
    def getCurrentUser(parent=None):
        dialog = UserChangeWindow(parent)
        result = dialog.exec_()
        return dialog.switch


        
        





if __name__ == "__main__":
    # print(userInfoFilePath)
    # initAdmin(userInfoFilePath)
    # pk_file = open(userInfoFilePath,'rb')

    # g = pickle.load(pk_file)
    # pk_file.close()

    # for i in g:
    #     print(i)

    app = QApplication(sys.argv)
    demo = UserChangeWindow()
    demo.show()
    sys.exit(app.exec_())
