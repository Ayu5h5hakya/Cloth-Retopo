import maya.cmds as mc

def showUI():
    window = mc.window(title="Layer utilities", widthHeight=(400,400))
    mc.columnLayout()
    mc.text(label="Collection of shortcut for layer related tasks")
    mc.showWindow(window)

showUI()