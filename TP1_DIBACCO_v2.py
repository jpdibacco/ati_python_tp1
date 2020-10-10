



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
xform = ".xform"
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
        cmds.setAttr(f + n + s + scaleX,size)
        cmds.setAttr(f + n + s + scaleY,1)
        cmds.setAttr(f + n + s + scaleZ,size)
        #add the obcjects inside the groups:
        cmds.parent(f+n+s,gname+ fu , relative=True )


#pilars constructor:

def makePilars(amount, initX, initZ, name, size, gname):
    for i in range(amount):
        s = str(i)
        cmds.polyCube(n='fb'+s,sx=5, sy=5, sz=5)
        cmds.setAttr('fb'+s + scaleY,1)
        cmds.setAttr('fb'+s + scaleX,3)
        cmds.setAttr('fb'+s + scaleZ,3)
        cmds.polyCylinder(n='fc'+s, h=0.5)
        cmds.setAttr('fc'+s + scaleX,1.5)
        cmds.setAttr('fc'+s + scaleZ,1.5)
        cmds.polyCylinder(n='fa'+s, sx=12, sy=12, sz=5, h=3)
        cmds.move(10,5,10+i*2,'fb'+s)
        cmds.move(10,5.8,10+i*2,'fc'+s)
        cmds.move(10,7.5,10+i*2,'fa'+s)
        # add a second pilar rotated by random:
        cmds.polyCylinder(n='fd'+s, sx=12, sy=12, sz=5, h=1.5)
        cmds.move(10,9.7,10+i*2,'fd'+s)
        cmds.rotate( 0, '12deg', 0, 'fd'+s)
        #add a third pilar:
        cmds.polyCylinder(n='fe'+s, sx=12, sy=12, sz=5, h=3)
        cmds.move(10,12,10+i*2,'fe'+s)
        # top part:
        cmds.polyCylinder(n='fg'+s, h=0.5)
        cmds.setAttr('fg'+s + scaleX,1.5)
        cmds.setAttr('fg'+s + scaleZ,1.5)
        cmds.polyCube(n='ff'+s,sx=5, sy=5, sz=5)
        cmds.setAttr('ff'+s + scaleY,1)
        cmds.setAttr('ff'+s + scaleX,3)
        cmds.setAttr('ff'+s + scaleZ,3)
        cmds.move(10,13.8,10+i*2,'fg'+s)
        cmds.move(10,14.5,10+i*2,'ff'+s)
        cmds.parent(f+n+s,gname+ fu , relative=True )
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
#makeGroup('pilar',1)
# let's make the stones:

for i in range (len(cubeNames)):
    makeStonesP(20,-30+i*3.1,-30,cubeNames[i],'a',1,3,'floor')
    makeStonesP(20,-28+i*2.8,-28,cubeNames[i],'b',2,2.7, 'floor')
    makeStonesP(20,-25+i*2.4,-25,cubeNames[i],'c',3,2.3, 'floor')
    makeStonesP(15,-28+i*2.2,-15,cubeNames[i],'d',4,2.1, 'floor')

# for i in range(1,2):
#     s = str(i)
#     cmds.polyCube(n='fb'+s,sx=5, sy=5, sz=5)
#     cmds.setAttr('fb'+s + scaleY,1)
#     cmds.setAttr('fb'+s + scaleX,3)
#     cmds.setAttr('fb'+s + scaleZ,3)
#     cmds.polyCylinder(n='fc'+s, h=0.5)
#     cmds.setAttr('fc'+s + scaleX,1.5)
#     cmds.setAttr('fc'+s + scaleZ,1.5)
#     cmds.polyCylinder(n='fa'+s, sx=12, sy=12, sz=5, h=3)
#     cmds.move(10,5,10+i*2,'fb'+s)
#     cmds.move(10,5.8,10+i*2,'fc'+s)
#     cmds.move(10,7.5,10+i*2,'fa'+s)

#     # add a second pilar rotated by random:

#     cmds.polyCylinder(n='fd'+s, sx=12, sy=12, sz=5, h=1.5)
#     cmds.move(10,9.7,10+i*2,'fd'+s)
#     cmds.rotate( 0, '12deg', 0, 'fd'+s)
#     #add a third pilar:

#     cmds.polyCylinder(n='fe'+s, sx=12, sy=12, sz=5, h=3)
#     cmds.move(10,12,10+i*2,'fe'+s)
#     # top part:

#     cmds.polyCylinder(n='fg'+s, h=0.5)
#     cmds.setAttr('fg'+s + scaleX,1.5)
#     cmds.setAttr('fg'+s + scaleZ,1.5)
#     cmds.polyCube(n='ff'+s,sx=5, sy=5, sz=5)
#     cmds.setAttr('ff'+s + scaleY,1)
#     cmds.setAttr('ff'+s + scaleX,3)
#     cmds.setAttr('ff'+s + scaleZ,3)
#     cmds.move(10,13.8,10+i*2,'fg'+s)
#     cmds.move(10,14.5,10+i*2,'ff'+s)


   # cmds.rotate( 0, '12deg', 0, 'fd'+s) no rotation
#cmds.setAttr('pCylinder1.scaleX',10)