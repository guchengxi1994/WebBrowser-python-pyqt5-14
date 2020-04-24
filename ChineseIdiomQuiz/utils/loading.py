'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-24 09:38:05
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-24 10:10:58
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel
import sys

class ProBar(QDialog):
    def __init__(self):
        super(ProBar,self).__init__()
        self.setFixedWidth(200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressbar = QProgressBar(self)                   # 1
        # self.progressbar.setOrientation(Qt.AlignCenter)          
        self.progressbar.setMinimum(0)                          # 2
        self.progressbar.setMaximum(100)
        self.progressbar.setRange(0, 100)
        self.progressbar.setFixedWidth(195)

        self.progressbar.move(10,5)

        self.status = QLabel("正在加载词库...",self)
        self.status.move(55,30)

        # self.setCentralWidget(self.progressbar)

        
        self.step = 0                                           # 3
        
        self.timer = QTimer(self)                               # 4
        self.timer.timeout.connect(self.update_func)
 

        self.start_stop_func()
        self.update_func()
 
    def start_stop_func(self):
        self.timer.start(35)
        # if self.ss_button.text() == 'Start':
        #     self.ss_button.setText('Stop')
        #     self.timer.start(100)
        # else:
        #     self.ss_button.setText('Start')
        #     self.timer.stop()
 
    def update_func(self):
        self.step += 1
        self.progressbar.setValue(self.step)

        if self.step>85:
            self.status.setText("正在加载主界面...")

        if self.step>=100:
            self.close()

    
    @staticmethod
    def start(parent=None):
        dialog = ProBar()
        result = dialog.exec_()
        return result
        # return dialog.ps
 
        # if self.step >= 100:
        #     self.ss_button.setText('Start')
        #     self.timer.stop()
        #     self.step = 0
 
    # def reset_func(self):
    #     self.progressbar.reset()
    #     self.ss_button.setText('Start')
    #     self.timer.stop()
    #     self.step = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ProBar()
    demo.show()
    sys.exit(app.exec_())


        

