#!/usr/bin/python
#-*- coding=utf-8 -*-
import os
import sys
#r"D:\work\ple" in sys.path or sys.path.append(r"D:\work\ple")
sys.path.append(r"G:\work\diy\20181023")
sys.path.append(r"D:\work\DQ\DQ_work\dq_work")
sys.path.append(r"/home/pi/share/code")
import time
from mojing.ui.head import *

#from Vegetation.ui.ui_main_window import ui_main_window

from mojing.ui.ui_mojing_widget import ui_mojing_widget
import mojing.env.Config as Config
reload(Config)
import mojing.core.work_response as wr
reload(wr)
import mojing.util.speak_think as speak_think
import time

#time.sleep(5)

import logging

# print "kaihsi log!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# logging.basicConfig(level=logging.WARNING,
#                     filename='/home/pi/share/code/tmp/log.txt',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # use logging
# logging.info('log start !!!!!')
# print "voer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

class BigWorkThread(QThread):
    """docstring for BigWorkThread"""

    def __init__(self, parent=None):
        super(BigWorkThread, self).__init__(parent)

    def setmywork(self, workfun):
        self.dosometings = workfun

    def run(self):
        self.dosometings()


class Response(QMainWindow):
    def __init__(self, parent = None):
        super(Response,self).__init__(parent)
        #self.setWindowTitle(_fromUtf8("发布工具"))
        self.maya_win=parent
        self.ImageinfoLib={}
        self.limit_list=[[]]
        self.pub_mod = False
        self.current_state=''
        self.setWindowTitle("mojing")
        self.setupUi()
        self.getElems()

        #self.setDefault()
        #self.setupConnections()
        #self.setDefault()
    def setupUi(self):
        self.ui_mojing_widget=ui_mojing_widget()

        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(),screen.height()+50)
        self.setGeometry(3,-10,screen.width()-10,screen.height())
        self.setCentralWidget(self.ui_mojing_widget)
        self.setWindowFlags(Qt.CustomizeWindowHint)
    def getElems(self):

        self.words_info_label_bel = self.ui_mojing_widget.main_Widget.words_info_label

    def set_label(self):
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.white)  #
        self.words_info_label_bel.setPalette(pe)
        font = QFont()
        #font.setFamily("Helvetica")
        font.setPixelSize(50)
        font.setBold(True)
        self.words_info_label_bel.setFont(font)
        pass
    def setDefault(self):
        self.set_label()
        QApplication.processEvents()
        speak_think.go(self.out_info)

    def setupConnections(self):
        pass
    def out_info(self,text):
        self.words_info_label_bel.setText(text)
        QApplication.processEvents()
        time.sleep(0.1)



if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    #app.setStyle('windows')
    # app.setStyleSheet('QMainWindow{border:1px solid rgb(45,45,45); background:rgb(45,45,45);}\
    #                 QMessageBox{background:rgb(45,45,45);}\
    #                 QLabel{color:rgb(200, 200, 200)}    \
    #                 QPushButton{background:rgb(90, 0, 0);color:rgb(100, 100, 100); width:49px; height:30px} \
    #                 QComboBox{border:3px solid rgb(45, 45, 45);background:rgb(50, 50, 50); color:rgb(180,180,180)}\
    #                 QListWidget{border:1px solid rgb(45,45,45); background:transparent}\
    #                 #QTreeWidget{border:1px solid rgb(30,30,30); background:transparent}\
    #                 QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
    #                 #QTreeWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(0,0,0); padding:15px} \
    #                 QListWidget::item{border:3px solid rgb(45, 45, 45); background:rgb(50, 50, 50); color:rgb(180,180,180); padding:15px}  \
    #                 QListWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(45,45,45); padding:15px} \
    #                 QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
    #                 QListView::item:selected:active{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:12px} \
    #                 QScrollBar:vertical {border: 2px solid rgb(80, 80, 80);background:rgb(50, 50, 50); width:20px; margin: 22px 0 22px 0;} \
    #                 QScrollBar::handle:vertical {background:rgb(95, 95, 95); min-height: 20px;}\
    #                 QScrollBar::add-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
    #                                                 subcontrol-position: bottom;subcontrol-origin: margin;}\
    #                 QScrollBar::sub-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
    #                                                 subcontrol-position: top;subcontrol-origin: margin;}\
    #                 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {border: 1px solid rgb(80, 80, 80); \
    #                                                 width:4px; height:4px; background:rgb(50, 50, 50);}\
    #                 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}\
    #                 ')
    app.setStyleSheet('QMainWindow{border:1px solid rgb(0,0,0); background:rgb(0,0,0);}\QPushButton{background:rgb(0,0,0);color:rgb(0,0,0)}; QLabel{color:rgb(200, 200, 200)}')
    print "init  Response !!!!"
    ui = Response()
    print "init  show  !!!!"
    ui.show()
    #QApplication.processEvents()

    #time.sleep(2)    # A=BigWorkThread()
    # A.setmywork(ui.setDefault)
    # A.start()
    ui.setDefault()
    sys.exit(app.exec_())