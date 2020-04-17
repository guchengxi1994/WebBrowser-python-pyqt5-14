'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 10:26:20
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 15:26:14
'''
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import sys

class CheckColumn(QWidget):
    

    def __init__(self,columns:list):
        super().__init__()       
        self.columns = columns
        self.initUI()
        self.ps = []

    def initUI(self):
        #新建4个复选框对象
        s = len(self.columns)
        if s > 0:
            self.varDict = locals()
            self.varDict['self.c_all'] = QCheckBox('全选',self)
            self.varDict['self.c_all'].move(20,20)
            self.varDict['self.c_all'].stateChanged.connect(self.change_all)
            height = 0
            
            for i in range(0,s):
                # print(self.columns[i])
                height = 20+(i+1)*20
                self.varDict['self.c_'+str(i)] = QCheckBox(self.columns[i],self)
                self.varDict['self.c_'+str(i)].move(30,height)
                # self.cb1 = QCheckBox('全选',self)
                # self.cb2 = QCheckBox('你是',self)
                # self.cb3 = QCheckBox('我的',self)
                # self.cb4 = QCheckBox('宝贝',self)
                self.varDict['self.c_'+str(i)].stateChanged.connect(self.stateClicked)
                # self.QHBox_whole.addWidget(self.createVar['self.c_'+str(i)]);

            self.bt = QPushButton('提交',self) 
            self.bt.move(120,height+50)
            self.bt.clicked.connect(self.sendData)

        self.resize(300,height+100)
        # self.setWindowTitle('早点毕业吧--复选框')

        # self.cb1.move(20,20)
        # self.cb2.move(30,50)
        # self.cb3.move(30,80)
        # self.cb4.move(30,110)

            
       
        #每当复选框的状态改变时，即每当用户选中或取消选中该信号时，就会发出此信号。所以当产生此信号的时候，我们将其连接相应的槽函数。其中全选（cb1）那个复选框对应的是changecb1，其它的是changecb2。
      
        # self.cb1.stateChanged.connect(self.changecb1)
        # self.cb2.stateChanged.connect(self.changecb2)
        # self.cb3.stateChanged.connect(self.changecb2)
        # self.cb4.stateChanged.connect(self.changecb2)
        # bt.clicked.connect(self.go)

        self.show()
    
        #当按钮被点击之后，根据复选框被选中的类型及数量，我们弹出了不同的信息。

    
     
    # def go(self):
    #     if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
    #         QMessageBox.information(self,'I Love U','你是我的宝贝！')
    #     elif self.cb2.isChecked() and self.cb3.isChecked():
    #         QMessageBox.information(self,'I Love U','你是我的！')
    #     elif self.cb2.isChecked() and self.cb4.isChecked():
    #         QMessageBox.information(self,'I Love U','你是宝贝！')
    #     elif self.cb3.isChecked() and self.cb4.isChecked():
    #         QMessageBox.information(self,'I Love U','我的宝贝！')
    #     elif self.cb2.isChecked():
    #         QMessageBox.information(self,'I Love U','你是！')
    #     elif self.cb3.isChecked():
    #         QMessageBox.information(self,'I Love U','我的！')
    #     elif self.cb4.isChecked():
    #         QMessageBox.information(self,'I Love U','宝贝！') 
    #     else:
    #         QMessageBox.information(self,'I Love U','貌似你没有勾选啊！')

    def change_all(self):
        if self.varDict['self.c_all'].checkState() == Qt.Checked:
            for i,j in self.varDict.items():

                if i=='s' or i=='self':
                    continue
                j.setChecked(True)
                self.ps = self.columns
        else:
            for i,j in self.varDict.items():
                if i=='s' or i=='self':
                    continue
                j.setChecked(False)
                self.ps.clear()

    
    
    def stateClicked(self):
        ss = set()
        for i,j in self.varDict.items():
            
            if i=='s' or i=='self':
                continue
            lp=self.varDict[i]
            if lp.isChecked():
                ss.add(lp.text())
        
        self.ps = list(ss)
            
            # if lp.isChecked():
            # # self.ps.append(lp.text())
            #     print(lp.text())
            # print("================")
    
        # print(self.ps)

    def sendData(self):
        # from .params import CheckParam
        # CheckParam = self.ps
        self.close()
        # mySignal = pyqtSignal(list)
        # return self.ps
        # mySignal.emit(self.ps)

    def sendData2(self):
        return self.ps

 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckColumn(["X","Y","Z"])
    sys.exit(app.exec_())
