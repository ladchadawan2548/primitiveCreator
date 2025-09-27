try:
    from PySide2 import QtCore, QtGui, QtWidgets
    from shiboken2 import wrapInstance

except :
    from PySide import QtCore, QtGui, QtWidgets
    from shiboken import wrapInstance

import maya.OpenMayaUI as omui

class PrimitiveCreatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        
        self.resize(380, 300)
        self.setWindowTitle("Primitive Creator")
 

def run():
    global ui

    try:
        ui.close()
    except:
        pass

    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = PrimitiveCreatorDialog(parent=ptr)
    ui.show()
