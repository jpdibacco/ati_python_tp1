import maya.cmds as cmds

# some common vars:
ultra = 70
bigger = 50
big = 40
medium = 20
small = 10
smaller = 5
scaleX = ".scaleX"
scaleY = ".scaleY"
scaleZ = ".scaleZ"

# array of names:

cubeNames = ['cubeA','cubeB','cubeC','cubeD', 'cubeE', 'cubeF', 'cubeG', 'cubeH', 'cubeI', 'cubeJ', 'cubeK','cubeL', 'cubeM', 'cubeN', 'cubeO', 'cubeP', 'cubeQ', 'cubeR','cubeS', 'cubeT']




## base for the temple:
cmds.polyPlane()
cmds.setAttr('pPlane1.scaleX',ultra)
cmds.setAttr('pPlane1.scaleZ',ultra)

#make it stone by stone:

for i in range(len(cubeNames)):
    s = str(i)
    # first middle row:
    cmds.polyCube(name=cubeNames[0]+s)
    cmds.move(0,1,-30 + i*3.1)
    cmds.setAttr(cubeNames[0]+s+scaleX,3)
    cmds.setAttr(cubeNames[0]+s+scaleY,1)
    cmds.setAttr(cubeNames[0]+s+scaleZ,3)
    cmds.polyCube(name=cubeNames[1]+s)
    cmds.move(-30+i*3.1,1,0)
    cmds.setAttr(cubeNames[1]+s+scaleX,3)
    cmds.setAttr(cubeNames[1]+s+scaleY,1)
    cmds.setAttr(cubeNames[1]+s+scaleZ,3)
    cmds.polyCube(name=cubeNames[2]+s)
    cmds.move(-30+i*3.1,1,3.1)
    cmds.setAttr(cubeNames[2]+s+scaleX,3)
    cmds.setAttr(cubeNames[2]+s+scaleY,1)
    cmds.setAttr(cubeNames[2]+s+scaleZ,3)
    


