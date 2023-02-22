import maya.cmds as mc

global layerNameField
global noRecurseField

def createLayer(args):
    global layerNameField
    global noRecurseField
    layerName = mc.textField(layerNameField, query=True, text=True)
    noRecurseFlag = mc.checkBox(noRecurseField, query = True, value=True)
    mc.createDisplayLayer(noRecurse=noRecurseFlag, name=layerName)

def showUI():
    global layerNameField
    global noRecurseField
    window = mc.window(title="Layer utilities", widthHeight=(400,400))
    mc.columnLayout()
    mc.text(label="Collection of shortcut for layer related tasks")
    mc.text(label="Layer name")
    layerNameField = mc.textField() 
    noRecurseField = mc.checkBox( label='Add children to layer' )
    mc.button(label="Create", command = createLayer, enable = True) 
    mc.showWindow(window)

showUI()