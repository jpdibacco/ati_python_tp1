



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
    cmds.move(initX,5,initZ+amount*5,'a'+name+s)
    cmds.parent('a'+name+s,gname + fu, relative=True)

def makeColumnsBase_b(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    #base:
    cmds.polyCylinder(n='b'+name + s, h=0.5)
    cmds.setAttr('b'+name+s + scaleX,1.5)
    cmds.setAttr('b'+name+s + scaleZ,1.5)
    cmds.move(initX,5.8,initZ+amount*5,'b'+name+s)
    cmds.parent('b'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pa(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='c'+name+s, sx=12, sy=12, sz=5, h=3)
    cmds.move(initX,7.5,initZ+amount*5,'c'+name+s)
    cmds.parent('c'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pb(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='d'+name+s, sx=12, sy=12, sz=5, h=1.5)
    cmds.move(initX,9.7,initZ+amount*5,'d'+name+s)
    cmds.rotate( 0, '12deg', 0, 'd'+name+s)
    cmds.parent('d'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pc(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='e'+name+s, sx=12, sy=12, sz=5, h=3)
    cmds.move(initX,12,initZ+amount*5,'e'+name+s)
    cmds.parent('e'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pd(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCylinder(n='g'+name+s, h=0.5)
    cmds.setAttr('g'+name+s + scaleX,1.5)
    cmds.setAttr('g'+name+s + scaleZ,1.5)
    cmds.move(initX,13.8,initZ+amount*5,'g'+name+s)
    cmds.parent('g'+name+s,gname + fu, relative=True)

def makeColumnsBase_Pe(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.polyCube(n='f'+name+s,sx=5, sy=5, sz=5)
    cmds.xform('f'+name+s, s =(3,1,3))
    cmds.move(initX,14.5,initZ+amount*5,'f'+name+s)
    cmds.parent('f'+name+s,gname + fu, relative=True)

#simple function to create the groups:
def makeGroup(name,num):
    f = str(num)
    cmds.group( em=True, n=name+f )

# let's make a loop with the function:
makeGroup('floor',1)
makeGroup('floor',2)
makeGroup('floor',3)
makeGroup('floor',4)
makeGroup('column',1)
makeGroup('column',2)
makeGroup('column',3)
#build the floor base:

for i in range (len(cubeNames)):
    makeStonesP(20,-30+i*3.1,-30,cubeNames[i],'a',1,3,'floor')
    makeStonesP(20,-28+i*2.8,-28,cubeNames[i],'b',2,2.7, 'floor')
    makeStonesP(20,-25+i*2.4,-25,cubeNames[i],'c',3,2.3, 'floor')
    makeStonesP(15,-28+i*2.2,-15,cubeNames[i],'d',4,2.1, 'floor')

#try to move group:
cmds.move(5,0,0,'floor4')
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


#this time I'll move the group because I'm tired:
cmds.move(-13,0,-25,'column3')
cmds.rotate( 0, '90deg', 0, 'column3')
cmds.duplicate( 'column3' )
cmds.move(-13,0,25,'column4')
cmds.rotate( 0, '90deg', 0, 'column4')