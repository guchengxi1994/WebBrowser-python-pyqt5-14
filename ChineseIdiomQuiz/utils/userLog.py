'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 16:54:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-26 17:16:47
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit
import sys,os
import pickle
from pypinyin import pinyin

BASE_DIR = os.path.abspath(os.curdir)
parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
userInfoFilePath = parent_Base_dir + os.sep + "static" + os.sep + "userInfo.pkl"


class UserInfo(object):
    def __init__(self,username,password,userlevel,email):
        self.username = username
        self.password = password
        self.userlevel = userlevel
        self.email = email
    
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
        




class UserLogWindow(QDialog):
    def __init__(self):
        super(UserLogWindow,self).__init__()


if __name__ == "__main__":
    # print(userInfoFilePath)
    initAdmin(userInfoFilePath)
    pk_file = open(userInfoFilePath,'rb')

    g = pickle.load(pk_file)
    pk_file.close()

    for i in g:
        print(i)

