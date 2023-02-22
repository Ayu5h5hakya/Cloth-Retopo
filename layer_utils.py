import maya.cmds as mc

global layerNameField

def showUI():
    window = mc.window(title="Layer utilities", widthHeight=(400,400))
    mc.columnLayout()
    mc.text(label="Collection of shortcut for layer related tasks")
    mc.text(label="Layer name")
    layerNameField = mc.textField() 

    mc.showWindow(window)

showUI()