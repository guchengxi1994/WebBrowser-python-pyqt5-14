'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-23 17:13:51
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-23 17:21:38
'''
from PyQt5.QtWidgets import QVBoxLayout,QRadioButton,\
    QPushButton,QMessageBox,QDialog


class MyDialog_GameMode_chosen(QDialog):
    def __init__(self,parent=None):
        super(MyDialog_GameMode_chosen,self).__init__(parent)
        self.setWindowTitle('RadioBoxDialog')
        self.vbox = QVBoxLayout(self)
        # self.hbox = QHBoxLayout(self)

        self.info1 = ''

        self.rb1 = QRadioButton('Mode1-->计时',self)
        self.rb2 = QRadioButton('Mode2-->倒计时',self)
        self.rb3 = QRadioButton('Mode3-->无计时',self)

        self.bt1 = QPushButton('提交',self)
        self.bt1.clicked.connect(self.ok)

        # self.bt1.move(20,120)

        self.vbox.addWidget(self.rb1)
        self.vbox.addWidget(self.rb2)
        self.vbox.addWidget(self.rb3)
        self.vbox.addWidget(self.bt1)

    

    def ok(self):
        # self.info1 = ""
        # pass
        if self.rb1.isChecked():
            self.info1 = self.rb1.text()
        elif self.rb2.isChecked():
            self.info1 = self.rb2.text()
        elif self.rb3.isChecked():
            self.info1 = self.rb3.text()
        # print("===============>"+self.info1)
        else:
            self.info1 = self.rb1.text()
            QMessageBox.warning(self, "警告对话框", "将默认使用计时模式！！", QMessageBox.Yes )
        self.close()

        # print(self.info1)




    @staticmethod
    def getData(options,parent=None):
        dialog = MyDialog_GameMode_chosen(parent)
        result = dialog.exec_()
        return dialog.info1