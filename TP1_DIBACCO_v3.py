



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
counter = 0
## base for the temple:
cmds.polyPlane()
cmds.setAttr('pPlane1.scaleX',ultra)
cmds.setAttr('pPlane1.scaleZ',ultra)

#make it stone by stone using a function:
def makeStonesP(amount, initX, initZ, name, floor, fuu, size,gname):
#fuu is not "fuu" is just a number for the floor
#convert some ints into strings:
    n = str(name)
    f = str(floor)
    fu = str(fuu)
#for loop:
    for i in range(amount):
        # first row:
        s = str(i)
        cmds.polyCube(name = f + n + s)
        cmds.move( initX, fuu, initZ + i * (size+0.1), f + n + s)
        cmds.xform(f + n + s, s = (size,1,size))
        #add the obcjects inside the groups:
        cmds.parent(f+n+s,gname+ fu , relative=True )

def makeColumnsBase(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    #base:
    cmds.polyCube(n='a'+name+s,sx=5, sy=5, sz=5)
    cmds.xform('a'+name+s, s =(3,1,3))
    cmds.move(10,5,10+amount*3,'a'+name+s)
    cmds.parent('a'+name+s,gname + fu, relative=True)

        # cmds.polyCylinder(n='b'+name + s, h=0.5)
        # cmds.setAttr('b'+name+s + scaleX,1.5)
        # cmds.setAttr('b'+name+s + scaleZ,1.5)
        # cmds.move(10,5.8,10+i*3,'b'+name+s)
        # cmds.polyCylinder(n='c'+name+s, sx=12, sy=12, sz=5, h=3)
        # cmds.move(10,7.5,10+i*3,'c'+name+s)
        #  # add a second pilar rotated by 12 deg, maybe later we can use some random funct:
        # cmds.polyCylinder(n='d'+name+s, sx=12, sy=12, sz=5, h=1.5)
        # cmds.move(10,9.7,10*2,'d'+name+s)
        # cmds.rotate( 0, '12deg', 0, 'd'+name+s)
        # #add a third pilar:
        # cmds.polyCylinder(n='e'+name+s, sx=12, sy=12, sz=5, h=3)
        # cmds.move(10,12,10+i*3,'e'+name+s)
        # # top part:
        # cmds.polyCylinder(n='g'+name+s, h=0.5)
        # cmds.setAttr('g'+name+s + scaleX,1.5)
        # cmds.setAttr('g'+name+s + scaleZ,1.5)
        # cmds.move(10,13.8,10+i*3,'g'+name+s)
        # cmds.polyCube(n='f'+name+s,sx=5, sy=5, sz=5)
        # cmds.xform('f'+name+s, s =(3,1,3))
        # cmds.setAttr('f'+name+s + scaleY,1)
        # cmds.setAttr('f'+name+s + scaleX,3)
        # cmds.setAttr('f'+name+s + scaleZ,3)
        # cmds.move(10,14.5,10+i*3,'f'+name+s)
        # #group parents:
        
        # cmds.parent('b'+name+s,gname + fu, relative=True)
        # cmds.parent('c'+name+s,gname + fu, relative=True)
        # cmds.parent('d'+name+s,gname + fu, relative=True)
        # cmds.parent('e'+name+s,gname + fu, relative=True)
        # cmds.parent('g'+name+s,gname + fu, relative=True)
        # cmds.parent('f'+name+s,gname + fu, relative=True)
#simple function to create the groups:
def makeGroup(name,num):
    f = str(num)
    cmds.group( em=True, n=name+f )

# array of names:

cubeNames = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

# let's make a loop with the function:
makeGroup('floor',1)
makeGroup('floor',2)
makeGroup('floor',3)
makeGroup('floor',4)
makeGroup('column',1)

#build the floor base:

for i in range (len(cubeNames)):
    makeStonesP(20,-30+i*3.1,-30,cubeNames[i],'a',1,3,'floor')
    makeStonesP(20,-28+i*2.8,-28,cubeNames[i],'b',2,2.7, 'floor')
    makeStonesP(20,-25+i*2.4,-25,cubeNames[i],'c',3,2.3, 'floor')
    makeStonesP(15,-28+i*2.2,-15,cubeNames[i],'d',4,2.1, 'floor')

#build the columns:

for i in range(1,10):
    s = str(i)
    makeColumnsBase(i, 1 ,1 ,'Corinthian'+s, 5, 'column', 1)