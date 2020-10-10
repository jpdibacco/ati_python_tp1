import maya.cmds as cmds
# some common vars:
ultra = 120
bigger = 50
big = 40
medium = 20
small = 10
smaller = 5
scaleX = ".scaleX"
scaleY = ".scaleY"
scaleZ = ".scaleZ"
counter = 0
# list of letters:
cubeNames = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
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
    cmds.move(initX,5,initZ+amount*size,'a'+name+s)
    cmds.parent('a'+name+s,gname + fu, relative=True)

def makeColumnsBase_b(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    #base:
    cmds.polyCylinder(n='b'+name + s, h=0.5)
    cmds.setAttr('b'+name+s + scaleX,1.5)
    cmds.setAttr('b'+name+s + scaleZ,1.5)
    cmds.move(initX,5.8,initZ+amount*size,'b'+name+s)
    cmds.parent('b'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pa(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='c'+name+s, sx=12, sy=12, sz=5, h=3)
    cmds.move(initX,7.5,initZ+amount*size,'c'+name+s)
    cmds.parent('c'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pb(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='d'+name+s, sx=12, sy=12, sz=5, h=1.5)
    cmds.move(initX,9.7,initZ+amount*size,'d'+name+s)
    cmds.rotate( 0, '12deg', 0, 'd'+name+s)
    cmds.parent('d'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pc(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='e'+name+s, sx=12, sy=12, sz=5, h=3)
    cmds.move(initX,12,initZ+amount*size,'e'+name+s)
    cmds.parent('e'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pd(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='g'+name+s, h=0.5)
    cmds.setAttr('g'+name+s + scaleX,1.5)
    cmds.setAttr('g'+name+s + scaleZ,1.5)
    cmds.move(initX,13.8,initZ+amount*size,'g'+name+s)
    cmds.parent('g'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pe(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCube(n='f'+name+s,sx=5, sy=5, sz=5)
    cmds.xform('f'+name+s, s =(3,1,3))
    cmds.move(initX,14.5,initZ+amount*size,'f'+name+s)
    cmds.parent('f'+name+s,gname + fu, relative=True)

#simple function to create the groups:
def makeGroup(name,num):
    f = str(num)
    cmds.group( em=True, n=name+f )

# let's make a loop with the function:
makeGroup('floor',1)
makeGroup('column',1)
makeGroup('column',2)
makeGroup('column',3)
#build the floor base:

for i in range (len(cubeNames)):
    makeStonesP(20,-30+i*3.1,-30,cubeNames[i],'a',1,3, 'floor')

#build the columns:

for i in range(1,7):
    s = str(i)
    #first 6 columns:
    makeColumnsBase(i, 15 ,-17 ,'Corinthian'+s, 5, 'column', 1)
    makeColumnsBase_b(i, 15 ,-17 ,'Corin'+s, 5, 'column', 1)
    makeColumnsBase_Pa(i, 15 ,-17 ,'Carin'+s, 5, 'column', 1)
    makeColumnsBase_Pb(i, 15 ,-17 ,'Rota'+s, 5, 'column', 1)
    makeColumnsBase_Pc(i, 15 ,-17 ,'Carin_b'+s, 5, 'column', 1)
    makeColumnsBase_Pd(i, 15 ,-17 ,'Top_a'+s, 5, 'column', 1)
    makeColumnsBase_Pe(i, 15 ,-17 ,'Top_b'+s, 5, 'column', 1)
    #second 6s c:
    makeColumnsBase(i, -19 ,-17 ,'Sorinthian'+s, 5, 'column', 2)
    makeColumnsBase_b(i, -19 ,-17 ,'Sorin'+s, 5, 'column', 2)
    makeColumnsBase_Pa(i, -19 ,-17 ,'Sarin'+s, 5, 'column', 2)
    makeColumnsBase_Pb(i, -19 ,-17 ,'Sota'+s, 5, 'column', 2)
    makeColumnsBase_Pc(i, -19 ,-17 ,'Sarin_b'+s, 5, 'column', 2)
    makeColumnsBase_Pd(i, -19 ,-17 ,'Sop_a'+s, 5, 'column', 2)
    makeColumnsBase_Pe(i, -19 ,-17 ,'Sop_b'+s, 5, 'column', 2)

for i in range(1,11):
    s = str(i)
    # this 10 columns:
    makeColumnsBase(i, -13 ,-17 ,'Gorinthian'+s, 5, 'column', 3)
    makeColumnsBase_b(i, -13 ,-17 ,'Gorin'+s, 5, 'column', 3)
    makeColumnsBase_Pa(i, -13 ,-17 ,'Garin'+s, 5, 'column', 3)
    makeColumnsBase_Pb(i, -13 ,-17 ,'Gota'+s, 5, 'column', 3)
    makeColumnsBase_Pc(i, -13 ,-17 ,'Garin_b'+s, 5, 'column', 3)
    makeColumnsBase_Pd(i, -13 ,-17 ,'Gop_a'+s, 5, 'column', 3)
    makeColumnsBase_Pe(i, -13 ,-17 ,'Gop_b'+s, 5, 'column', 3)


#some adjustments over the groups:
cmds.move(-13,0,-25,'column3')
cmds.rotate( 0, '90deg', 0, 'column3')
cmds.duplicate( 'column3' )
cmds.move(-13,0,0,'column4')
cmds.rotate( 0, '90deg', 0, 'column4')
cmds.duplicate( 'floor1')
cmds.duplicate( 'floor2')
cmds.duplicate( 'floor3')
cmds.move(0,1,0,'floor2')
#cmds.setAttr('floor2',s=2)
cmds.move(0,2,0,'floor3')
cmds.move(0,3,0,'floor4')
cmds.scale( 1.5, 1, 1.5, 'floor1')
cmds.scale( 1.4, 1, 1.4, 'floor2')
cmds.scale( 1.3, 1, 1.3, 'floor3')
cmds.scale( 1.2, 1, 1.2, 'floor4')
cmds.scale( 1.2, 1, 1.2, 'column1')
cmds.scale( 1.2, 1, 1.2, 'column2')
cmds.scale( 1.2, 1, 1.2, 'column3')
cmds.scale( 1.2, 1, 1.2, 'column4')
cmds.setAttr('column1.translateX',14)
cmds.setAttr('column2.translateX',-10)
cmds.setAttr('column3.translateZ',-30)

# build ceiling:

cmds.polyCube(n='rc', w=30)
cmds.rotate(0,'180deg',0,'rc')
cmds.scale(2.2,2,4, 'rc')
cmds.move(0,16,-15,'rc')
cmds.duplicate('rc')
cmds.move(0,16,17,'rc1')
cmds.duplicate('rc1')
cmds.rotate(0,'90deg',0,'rc2')
cmds.scale(1.2,2,4, 'rc2')
cmds.move(33,16,1,'rc2')
cmds.duplicate('rc2')
cmds.move(-33,16,1,'rc3')

makeGroup('minicolumn',1)
for i in range(1,4):
    s = str(i)
    makeColumnsBase(i, 15 ,-17 ,'m_Corinthian'+s, 2, 'minicolumn', 1)
    makeColumnsBase_b(i, 15 ,-17 ,'m_Corin'+s, 2, 'minicolumn', 1)
    makeColumnsBase_Pa(i, 15 ,-17 ,'m_Carin'+s, 2, 'minicolumn', 1)
    makeColumnsBase_Pb(i, 15 ,-17 ,'m_Rota'+s, 2, 'minicolumn', 1)
    makeColumnsBase_Pc(i, 15 ,-17 ,'m_Carin_b'+s, 2, 'minicolumn', 1)
    makeColumnsBase_Pd(i, 15 ,-17 ,'m_Top_a'+s, 2, 'minicolumn', 1)
    makeColumnsBase_Pe(i, 15 ,-17 ,'m_Top_b'+s, 2, 'minicolumn', 1)

cmds.scale(0.3,0.3,0.3,'minicolumn1')
cmds.move(-39,15.5,19,'minicolumn1')

# let's try to loop this...
for i in range(1,11):
    s = str(i)
    cmds.duplicate('minicolumn'+s)
    cmds.move(-39,15.5,19 - i*3,'minicolumn'+s)

for i in range(1,12):
    s = str(i)
    cmds.duplicate('minicolumn'+s)
    cmds.move(30,15.5,22 - i*3,'minicolumn'+s)

cmds.polyCube(n='techo')
cmds.move(0,18,1,'techo')
cmds.scale(69,3,36, 'techo')
cmds.duplicate('techo')
cmds.scale(72,1,38, 'techo1')
cmds.move(0,20.5,1,'techo1')
cmds.duplicate('techo1')
cmds.scale(68,1,19, 'techo2')
cmds.move(0,22.5,-8,'techo2')
cmds.duplicate('techo2')
cmds.move(0,22.5,10,'techo3')
cmds.rotate(16,0,0,'techo3')
cmds.rotate(-16,0,0,'techo2')