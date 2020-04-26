'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 16:54:12
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-26 16:59:42
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit
import sys

from pypinyin import pinyin

class UserInfo(object):
    def __init__(self,username,password,userlevel,email):
        self.username = username
        self.password = password
        self.userlevel = userlevel
        self.email = email


class UserLogWindow(QDialog):
    def __init__(self):
        super(UserLogWindow,self).__init__()