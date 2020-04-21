'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-16 15:40:21
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-21 13:52:05
'''
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,QFileDialog,QInputDialog,QMessageBox, \
    QCheckBox,QVBoxLayout,QHBoxLayout,QLabel,QDialog,QPushButton,QMenu, \
    QCompleter
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import Qt
import sys,os,requests
from PyQt5.QtWebEngineWidgets import QWebEngineView
import utils.repath as repath
from utils.analyse import *
from utils.checkParams import CheckColumn


BASE_DIR = os.path.abspath(os.curdir)



if os.path.exists(BASE_DIR + '/static/net.txt'):
    with open(BASE_DIR + '/static/net.txt', 'r', encoding='utf-8') as data:
        defaultUrl = data.readline()
        # print(defaultUrl)
else:
    # import pathlib
    # pathlib.Path(BASE_DIR + '/static/net.txt').touch()
    f = open(BASE_DIR + '/static/net.txt','w',encoding='utf-8')
    defaultUrl = "https://www.bing.com"
    f.write(defaultUrl)
    f.close()


def not_empty(s):
    """
    去除列表中None跟"", 参考：https://www.cnblogs.com/yspass/p/9434366.html
    """
    return s and s.strip() and s.replace("\n","") and s.replace("%0A","")


favWebs = []
if os.path.exists(BASE_DIR + '/static/storage.txt'):
    with open(BASE_DIR + '/static/storage.txt', 'r', encoding='utf-8') as data:
        # defaultUrl = data.readline()
        favWebs = list(data)
        favWebs = list(filter(not_empty,favWebs))
        # print(defaultUrl)
else:
    # import pathlib
    # pathlib.Path(BASE_DIR + '/static/net.txt').touch()
    f = open(BASE_DIR + '/static/storage.txt','w',encoding='utf-8')
    defaultUrl = "https://www.bing.com"
    f.write(defaultUrl+'\n')
    f.close()
    favWebs.append('https://www.bing.com')
    


class UI(QMainWindow,):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle('Web browser')
        self.resize(1280,960)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + '/static/imgs/sun.png'))
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(self.main_toolbar)
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs_layout = QtWidgets.QGridLayout()
        

        

        self.tabs.setLayout(self.tabs_layout)
        self.url_edit = QtWidgets.QLineEdit()
        self.cwd = BASE_DIR + "/LocalWebTest/static/"

        self.favWebs = favWebs
        
        self.browser = QWebEngineView()
        # Url = 'https://www.baidu.com'
        # Url = 'https://www.bing.com'
        Url = defaultUrl
        self.browser.setUrl(QtCore.QUrl(Url))
        self.tabs_layout.addWidget(self.browser)
        self.tabs.addTab(self.browser,'')
        self.browser.loadFinished.connect(lambda :self.tabs.setTabText(0,self.browser.page().title()))
        self.setCentralWidget(self.tabs)



        self.turn_button = QAction(QIcon(BASE_DIR + '/static/imgs/zhuandao.png'),'Turn',self)
        self.back_button = QAction(QIcon(BASE_DIR + '/static/imgs/fanhui.png'),'Back',self)
        self.next_button = QAction(QIcon(BASE_DIR + '/static/imgs/tiaozhuan.png'),'Forward',self)
        self.stop_button = QAction(QIcon(BASE_DIR + '/static/imgs/close.png'),'Stop',self)
        self.reload_button = QAction(QIcon(BASE_DIR + '/static/imgs/shuaxin.png'),'Reload',self)
        self.add_button = QAction(QIcon(BASE_DIR + '/static/imgs/add.png'),'Addpage',self)
        
        #DIY
        self.set_default_openPage_button = QAction(QIcon(BASE_DIR + '/static/imgs/lock.png'),'SetDefault',self)
        self.set_data_button = QAction(QIcon(BASE_DIR + '/static/imgs/data.png'),'AnalyzeData',self)
        self.set_test_button = QAction(QIcon(BASE_DIR + '/static/imgs/test.png'),'TestButton',self)
        self.set_store_button = QAction(QIcon(BASE_DIR + '/static/imgs/storage.png'),'storage',self)



        self.main_toolbar.addAction(self.back_button)
        self.main_toolbar.addAction(self.next_button)
        self.main_toolbar.addAction(self.stop_button)
        self.main_toolbar.addAction(self.reload_button)
        self.main_toolbar.addAction(self.add_button)
        self.main_toolbar.addWidget(self.url_edit)
        self.main_toolbar.addAction(self.turn_button)


        #DIY
        self.main_toolbar.addAction(self.set_default_openPage_button)
        self.main_toolbar.addAction(self.set_data_button)
        self.main_toolbar.addAction(self.set_store_button)
        #测试按钮
        self.main_toolbar.addAction(self.set_test_button)
        



        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.close)
        self.reload_button.triggered.connect(self.browser.reload)
        self.turn_button.triggered.connect(self.OpenUrlLine)
        self.browser.urlChanged.connect(self.setUrlLine)
        self.tabs.tabBarDoubleClicked.connect(self.NewPage)
        self.add_button.triggered.connect(self.NewPage)
        self.tabs.tabCloseRequested.connect(self.Closepage)

        #DIY
        self.set_default_openPage_button.triggered.connect(self.defaultPage)
        self.set_data_button.triggered.connect(self.anaData)
        self.set_store_button.triggered.connect(self.showFavs)
        #测试按钮
        self.set_test_button.triggered.connect(self.test)
        #回车事件判断
        self.url_edit.returnPressed.connect(self.inputTurn)
        #输入事件判断
        # self.url_edit.textChanged.connect(self.showHistory)
        self.showHistory()


    def  showHistory(self): 
        if os.path.exists(BASE_DIR + '/static/history.txt'):
            with open(BASE_DIR + '/static/history.txt', 'r', encoding='utf-8') as data:
                items_list = list(data)
                items_list = list(set(items_list))
                items_list = list(filter(not_empty,items_list))
        else:
            f = open(BASE_DIR + '/static/history.txt','w',encoding='utf-8')
            f.write("https://www.bing.com\n")
            f.close()
            items_list = ["https://www.bing.com"]

        self.completer = QCompleter(items_list)
        self.completer.setFilterMode(Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.url_edit.setCompleter(self.completer)







    def inputTurn(self):
        # print(self.url_edit.text())
        s = self.url_edit.text().strip().replace("%0A","")
        if s.startswith("http://") or s.startswith("https://"):
            self.browser.setUrl(QtCore.QUrl( self.url_edit.text()))
        else:
            self.browser.setUrl(QtCore.QUrl( 'http://'+ self.url_edit.text()))
        self.addHistory()

    
    def showDialog(self,options:list):
        from utils.checkParams import MyDialog_column_chosen
        from utils.checkParams import MyDialog_FigureType_chosen
        if len(options)>0:
            dialog_column = MyDialog_column_chosen(options)
            result = dialog_column.exec_()
            if len(dialog_column.ps)>0 :
                # print(dialog_column.ps)
                dialog_figureType = MyDialog_FigureType_chosen()
                retult = dialog_figureType.exec_()              
                return dialog_column.ps,dialog_figureType.info1
            else:
                dialog_figureType = MyDialog_FigureType_chosen()
                retult = dialog_figureType.exec_()              
                return options,dialog_figureType.info1
        else:
            QMessageBox.critical(self, "错误对话框", "表名错误或者为空表", QMessageBox.Yes )
            return [],""

       

    def showFavs(self):
        """
        显示收藏的网页
        """
        menu = QMenu()
        vDict = locals()
        s = len(self.favWebs)
        if s>0:
            for i in range(0,s):
                vDict['x'+str(i)] = menu.addAction(self.favWebs[i])
                vDict['x'+str(i)].triggered.connect(self.favWebTurn)      
        menu.exec_(QCursor.pos())



    def test(self):
        menu = QMenu()
        vDict = locals()
        s = len(self.favWebs)
        if s>0:
            for i in range(0,s):
                vDict['x'+str(i)] = menu.addAction(self.favWebs[i])
                vDict['x'+str(i)].triggered.connect(self.favWebTurn)

        
        menu.exec_(QCursor.pos())
        

        """
        ## 用来访问图片的代码，重要
        # import requests
        # url = 'http://localhost:5000/showImg'
        # img = '?imgName=D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\test.png'
        # self.browser.setUrl(QtCore.QUrl( url+img))
        """

    
    def mousePressEvent(self,event):
        if event.buttons () == QtCore.Qt.RightButton:
            if self.url_edit.text().startswith("http://localhost:5000/showImg"): 

                menu = QMenu()
                b1 = menu.addAction("修改X轴名")
                b2 = menu.addAction("修改Y轴名")
                b3 = menu.addAction("关于...")

                b3.triggered.connect(self.b3Clicked)
                b1.triggered.connect(self.b1Clicked)
                b2.triggered.connect(self.b2Clicked)
                menu.exec_(QCursor.pos())
            
            else:
                menu = QMenu()
                b4 = menu.addAction("收藏网页")
                b5 = menu.addAction("设为默认...")

                b4.triggered.connect(self.b4Clicked)
                b5.triggered.connect(self.b5Clicked)
                menu.exec_(QCursor.pos())

    

    def b3Clicked(self):
        QMessageBox.information(self, "提示：", '   作者很帅')

    def b1Clicked(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要修改的X轴名：')

    def b2Clicked(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要修改的Y轴名：')

    def b4Clicked(self):
        ss = set(self.favWebs)
        ss.add(self.url_edit.text())
        self.favWebs = list(ss)
        f = open(BASE_DIR + '/static/storage.txt','w',encoding='utf-8')

        for i in range(0,len(self.favWebs)):
            f.write(self.favWebs[i]+"\n")        
        f.close()

    def b5Clicked(self):
        text = self.url_edit.text()
        f = open(BASE_DIR+"/static/net.txt",'w',encoding='utf-8')
        if str(text).startswith("http://") or str(text).startswith("https://"):                      
            f.writelines(text)
        else:
            f.writelines("http://"+text) 
        f.close()

    def favWebTurn(self):
        # print(self.sender().text())
        s = self.sender().text().replace("\n","")
        self.url_edit.setText(s)
        self.addHistory()
        if s.startswith("http://") or s.startswith("https://"):
            self.browser.setUrl(QtCore.QUrl( self.url_edit.text()))
        else:
            self.browser.setUrl(QtCore.QUrl( 'http://'+ self.url_edit.text()))

    
    def addHistory(self):
        f = open(BASE_DIR + '/static/history.txt','a',encoding='utf-8')
        text = self.url_edit.text()
        f.writelines(text+"\n")
        f.close() 



    def anaData(self):
        # ps = []
        # import time
        """
        数据分析
        """
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        # print(fileName_choose)
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要分析的数据表名：')
        
        if ok:
            if text != "":
                sheetName = text
                # print(text)          
                options = readColumn(fileName_choose,sheetName=text)
                ps,formType = self.showDialog(options)
            else:
                sheetName = 'Sheet1'
                QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
                options = readColumn(fileName_choose,sheetName='Sheet1')
                # print(options)
                # self.showDialog(options)
                ps,formType = self.showDialog(options)
        else:
            sheetName = 'Sheet1'
            QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
            options = readColumn(fileName_choose,sheetName='Sheet1')
            ps,formType = self.showDialog(options)
        
        ps = list(set(ps))
        # print(ps)
        print(ps)
        if len(ps)>0 :
            figurePath = plotFigure(fileName_choose,sheetName,ps,formType)

            from utils.webTest import check_aliveness
            result = check_aliveness('127.0.0.1',5000)
            if result:
                import requests
                url = 'http://localhost:5000/showImg'
                img = '?imgName='+figurePath
                self.browser.setUrl(QtCore.QUrl( url+img))
            else:
                QMessageBox.warning(self, "警告对话框", "服务器未启动", QMessageBox.Yes )
            

        



    def defaultPage(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入默认网址：')
        if ok :
            if text != "":
                # print(text)
                if repath.judge(text):
                    # print(text)
                    f = open(BASE_DIR+"/static/net.txt",'w',encoding='utf-8')
                    if str(text).startswith("http://") or str(text).startswith("https://"):
                        
                        f.writelines(text)
                    else:
                        f.writelines("http://"+text)
                    
                    f.close()
                else:
                    QMessageBox.critical(self, "错误对话框", "你输入网址模式错误", QMessageBox.Yes )
            else:
                QMessageBox.warning(self, "警告对话框", "你未输入网址", QMessageBox.Yes )


    def setUrlLine(self,url):
        self.url_edit.setText(url.toString())

    def OpenUrlLine(self):
        self.urlline = self.url_edit.text()
        print(self.urlline)
        # self.url_edit.setText(url_edit)
        if self.urlline.startswith('http://') or self.urlline.startswith('https://'):
            self.browser.setUrl(QtCore.QUrl( self.urlline))
        else:
            self.browser.setUrl(QtCore.QUrl( "http://" +self.urlline))
        self.addHistory()


    def NewPage(self,url=defaultUrl,label=''):
        browser = QWebEngineView()
        # Url = 'https://cn.bing.com'
        Url = defaultUrl
        browser.setUrl(QtCore.QUrl(Url))
        i = self.tabs.addTab(browser,label)
        self.tabs.setCurrentIndex(i)
        print(i)

        browser.loadFinished.connect(lambda :self.tabs.setTabText(i,browser.page().title()))

    def Closepage(self,i):
        if self.tabs.count() == 1:  
            self.tabs.removeTab(i)
            self.NewPage()
        else:
            self.tabs.removeTab(i)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = UI()
    gui.show()
    sys.exit(app.exec_())