'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-20 14:30:48
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-20 14:32:52
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMenu,QMessageBox,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # 窗口标题
        self.setWindowTitle('右键菜单')
        # 定义窗口大小
        self.resize(400, 400)
        # 将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 创建QMenu信号事件
        self.customContextMenuRequested.connect(self.showMenu)
        self.contextMenu = QMenu(self)
        self.CP = self.contextMenu.addAction('复制')
        self.JQ = self.contextMenu.addAction('剪切')
        self.NT = self.contextMenu.addAction('粘贴')
        # 二级菜单
        self.GN = self.contextMenu.addMenu("功能")
        self.ZJ = self.GN.addAction('增加')
        self.XG = self.GN.addAction('修改')
        self.SC = self.GN.addAction('删除')
        # 事件绑定
        self.CP.triggered.connect(self.Event)
        self.JQ.triggered.connect(self.Event)
        self.NT.triggered.connect(self.Event)
        self.ZJ.triggered.connect(self.Event)
        self.XG.triggered.connect(self.Event)
        self.SC.triggered.connect(self.Event)
    def showMenu(self, pos):
        # pos 鼠标位置
        print(pos)
        # 菜单显示前,将它移动到鼠标点击的位置
        self.contextMenu.exec_(QCursor.pos())  # 在鼠标位置显示
    def Event(self):
        QMessageBox.information(self, "提示：", '   您选择了' + self.sender().text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())