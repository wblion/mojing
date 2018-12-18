# -*- coding: utf-8 -*-
#by wangbin 852854910
import sys
import os
# from PySide.QtCore import *
# from PySide.QtGui import *
import Vegetation.ui.head as head
from Vegetation.ui.head import *
class My_QToolButton(QToolButton):
    xxx = 0
    DoubledddClick = Signal()
    entertool = Signal()
    def __init__(self, parent=None,Text=None,icon=True,pass_floderpath=None,iteminfo={}):
        super(My_QToolButton,self).__init__(parent)
        self.icon=icon
        self.Text=Text
        self.iteminfo=iteminfo

        self.pass_floderpath=pass_floderpath
    def get_info(self):
        return self.iteminfo
    def enterEvent(self,event):
        self.entertool.emit()
    def mouseDoubleClickEvent (self,event):
        self.DoubledddClick.emit()
class my_show_widget(QWidget):
    def __init__(self, parent=None):
        super(my_show_widget,self).__init__(parent)
    def mousePressEvent (self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.glpos=QMouseEvent.globalPos()
            self.pos = QMouseEvent.pos()
    def get_chile_widget(self):
        #chile_widget=self.childAt(self.glpos)
        chile_widget = self.childAt(self.pos)
        return chile_widget

class ui_show_widget_item(QWidget):
    def __init__(self, parent=None,IcoPath=None,ImageSize=None,icon=True,Text=None,passfloderpath=None,iteminfo=None):
        super(ui_show_widget_item,self).__init__(parent)
        self.IcoPath=IcoPath
        self.ImageSize=ImageSize
        self.icon=icon
        self.Text=Text
        self.passfloderpath=passfloderpath
        self.iteminfo=iteminfo
        self.setupUi()
    def setupUi(self):
        self.mainVboxLayout=QVBoxLayout(self)
        self.ImageWidgetItem=My_QToolButton(Text=self.Text,icon=self.IcoPath,pass_floderpath=self.passfloderpath,iteminfo=self.iteminfo)
        IanmBUttonIcon=QIcon(QPixmap(self.IcoPath))
        #IanmBUttonIcon.iconSize(QSize(30,30))
        
        self.ImageWidgetItem.setIcon(IanmBUttonIcon)
        self.ImageWidgetItem.setIconSize(QSize(150,95))
        self.ImageWidgetItem.setAutoRaise(1)
        self.ImageWidgetItem.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ImageWidgetItem.setText(self.Text)

        ####
        self.ImageWidgetItem.setFixedSize(215,135)
        self.mainVboxLayout.addWidget(self.ImageWidgetItem)
        self.mainVboxLayout.setContentsMargins(0,0,0,0)


    def GetINfo(self):
        info_lib={}
        info_lib["IconPath"]=self.icon
        info_lib["TextName"]=self.Text
        return info_lib