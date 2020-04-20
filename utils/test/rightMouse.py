'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-20 15:27:11
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-20 16:02:49
'''

from PyQt5.QtWidgets import QMenu,QMainWindow,QApplication,QMessageBox, \
    QInputDialog
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor

# class MyMenu(QMenu):
#     def __init__(self):
#         # super.__init__()

#         self.b1 = self.addAction('操作1')
#         self.b2 = self.addAction('操作2')
#         self.b3 = self.addAction('操作3')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('右键菜单')
        # 定义窗口大小
        self.resize(400, 400)

    def mousePressEvent(self,event):
        # return super().mousePressEvent()
        if event.buttons () == QtCore.Qt.RightButton:                        # 右键按下
            # self.setText ("单击鼠标右键的事件: 自己定义")
            # print("单击鼠标右键")
            menu = QMenu()
            b1 = menu.addAction("修改X轴名")
            b2 = menu.addAction("修改Y轴名")
            b3 = menu.addAction("关于...")

            b3.triggered.connect(self.b3Clicked)
            b1.triggered.connect(self.b1Clicked)
            b2.triggered.connect(self.b2Clicked)
            menu.exec_(QCursor.pos())
    
    def b3Clicked(self):
        QMessageBox.information(self, "提示：", '   作者很帅')

    def b1Clicked(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要修改的X轴名：')

    def b2Clicked(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要修改的Y轴名：')


    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

        