'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 16:54:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-27 09:40:29
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit, \
    QMessageBox
import sys,os
import pickle
from pypinyin import pinyin

BASE_DIR = os.path.abspath(os.curdir)
parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
userInfoFilePath = parent_Base_dir + os.sep + "static" + os.sep + "userInfo.pkl"


class UserInfo(object):
    def __init__(self,username,password,userlevel,email,isLogged=False,isCurrentUser=True):
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

        u = UserInfo("admin",'admin',5,"admin@test.com")
        userSet.add(u)
        userList = list(userSet)

        pk_file = open(userInfoFilePath,'wb')
        pickle.dump(userList,pk_file)
        pk_file.close()
        

def loadUsers(userInfoFilePath):
    pk_file = open(userInfoFilePath,'rb')
    g = pickle.load(pk_file)
    pk_file.close()

    return g

def iterator2list(itera):
    res = []
    for i in itera:
        res.append(i)
    return res

class UserLogWindow(QDialog):
    def __init__(self):
        super(UserLogWindow,self).__init__()

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
                print(self.currentUser)
            else:
                QMessageBox.warning(self,'警告','用户名或者密码错误',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        





if __name__ == "__main__":
    # print(userInfoFilePath)
    # initAdmin(userInfoFilePath)
    # pk_file = open(userInfoFilePath,'rb')

    # g = pickle.load(pk_file)
    # pk_file.close()

    # for i in g:
    #     print(i)

    app = QApplication(sys.argv)
    demo = UserLogWindow()
    demo.show()
    sys.exit(app.exec_())
