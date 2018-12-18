import sys

sys.path.append(r"D:\git_work\vag\dq_work")
sys.path.append(r"D:\work\DQ\DQ_work\dq_work")

from Vegetation.ui.head import *
import maya.cmds as cmds
import maya.OpenMayaUI as apiUI
try:
    import shiboken2
except:
    import shiboken

#get maya windownhange pyqt lib
def getMayaWindow():
      ptr = apiUI.MQtUtil.mainWindow()
      try:
          wrap=shiboken2.wrapInstance(long(ptr), QWidget)
      except:
          wrap = shiboken.wrapInstance(long(ptr), QWidget)

      return wrap

def MayaLoadWind():
    for wnd in QApplication.topLevelWidgets():
        if not hasattr(wnd, 'isWindow'): continue  # if zhe windown is Exist
        if not wnd.isWindow(): continue
        if wnd.windowTitle() == 'MDL_library':  # if zhe windwon name is you windownn name
            wnd.setParent(None)
            wnd.deleteLater()
            '''
            wnd.show()#show window 
            wnd.activateWindow()#active windwon 
            '''
    maya_win=getMayaWindow()
    myWindow = ShowWindow(maya_win)  # if do not have windown and creat it
    return myWindow
    myWindow = ShowWindow()  # if do not have windown and creat it
    return myWindow


def ShowWindow(maya_win):
    import Vegetation.core.response as response
    reload(response)
    myWindow = response.Response(maya_win)
    myWindow.show()
    return myWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    A = ShowWindow()
    sys.exit(app.exec_())

'''
import sys
sys.path.append(r'D:\work\DQ\DQ_work\dq_work')
sys.path.append(r'D:\git_work\vag\dq_work')
import Vegetation.main.maya_load_win as maya_load_win
reload(maya_load_win)
ui = maya_load_win.MayaLoadWind()
'''