#for progress on this work check my public repo at: https://github.com/jpdibacco/ati_python_tp1
import maya.cmds as cmds
cmds.file(f=True, new=True)
# some common vars:
ultra = 240 # don't touch this
floorStones = 20 # don't touch this
scaleX = ".scaleX"
scaleY = ".scaleY"
scaleZ = ".scaleZ"
# list of letters:
cubeNames = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
# this is not elegant, just in case i run out of index:
columnNamesA = ['Corinthian','Corin','Carin','Rota','Carin_b','Top_a','Top_b', 'a_Ena','a_Dio','a_Tria','a_Tesera','a_Pende','a_Exi','a_Epta','a_Okto','a_Enea','a_Deka']
columnNamesB = ['b_Corinthian','b_Corin','b_Carin','b_Rota','b_Carin_b','b_Top_a','b_Top_b','b_Tria','b_Tesera','b_Pende','b_Exi','b_Epta','b_Okto','b_Enea','b_Deka']
columnNamesC = ['c_Corinthian','c_Corin','c_Carin','c_Rota','c_Carin_b','c_Top_a','c_Top_b','c_Malaka','c_Socrates','c_Tasos','c_Arostaky','c_Ena','c_Dio','c_Tria','c_Tesera','c_Pende','c_Exi','c_Epta','c_Okto','c_Enea','c_Deka']
columnNamesD = ['d_Corinthian','d_Corin','d_Carin','d_Rota','d_Carin_b','d_Top_a','d_Top_b']
columnNamesE = ['e_Corinthian','e_Corin','e_Carin','e_Rota','e_Carin_b','e_Top_a','e_Top_b']

## Create Window UI:

def createWindow():
    cmds.window(title = "Temple Generator © ATI", widthHeight=(450, 350))
    cmds.columnLayout()
    cmds.intSliderGrp("slider1", field=True, label='Temple Width', minValue=4, maxValue=10, value=7 )
    cmds.intSliderGrp("slider2", field=True, label='Temple Height', minValue=1, maxValue=10, value=1 )
    cmds.intSliderGrp("slider3", field=True, label='Temple Stairs', minValue=1, maxValue=5, value=2 )
    cmds.button(label = "Create Temple",c='buildTemple()')
    cmds.button(label = "Reset",c='cmds.file(f=True, new=True)')
    cmds.button(label="Fix plafond", c='fixPlafond()')
    cmds.showWindow()

## base for the temple:

def makeBase():
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
        cmds.instance('deletePolyCube', n = f + n + s)
        cmds.move( initX, fuu, initZ + i * (size+0.1), f + n + s)
        cmds.xform(f + n + s, s = (size,1,size))
        #add the obcjects inside the groups:
        cmds.parent(f+n+s,gname+ fu)

def makeColumnsBase(amount, initX, initZ, name, size, gname, gnumber):
    n = str(name)
    fu = str(gnumber)
    s = str(amount)
    cmds.instance('deleteComplexPolyCube', n = 'a' + name + s )
    cmds.xform('a'+name+s, s =(3,1,3))
    cmds.move(initX,5,initZ+amount*size,'a'+name+s)
    cmds.parent('a'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCylinder', n = 'b'+name +s)
    cmds.setAttr('b'+name+s + scaleX,1.5)
    cmds.setAttr('b'+name+s + scaleZ,1.5)
    cmds.move(initX,5.8,initZ+amount*size,'b'+name+s)
    cmds.parent('b'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCylinderC', n = 'c'+name +s)
    cmds.move(initX,7.5,initZ+amount*size,'c'+name+s)
    cmds.parent('c'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCylinderD', n = 'd'+name +s)
    cmds.move(initX,9.7,initZ+amount*size,'d'+name+s)
    cmds.rotate( 0, '12deg', 0, 'd'+name+s)
    cmds.parent('d'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCylinderC', n = 'e'+name +s)
    cmds.move(initX,12,initZ+amount*size,'e'+name+s)
    cmds.parent('e'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCylinder', n = 'g'+name +s)
    cmds.setAttr('g'+name+s + scaleX,1.5)
    cmds.setAttr('g'+name+s + scaleZ,1.5)
    cmds.move(initX,13.8,initZ+amount*size,'g'+name+s)
    cmds.parent('g'+name+s,gname + fu, relative=True)

    cmds.instance('deleteComplexPolyCube', n = 'f'+name +s)
    cmds.xform('f'+name+s, s =(3,1,3))
    cmds.move(initX,14.5,initZ+amount*size,'f'+name+s)
    cmds.parent('f'+name+s,gname + fu, relative=True)



#simple function to create the groups:
def makeGroup(name,num):
    f = str(num)
    cmds.group( em=True, n=name+f )


#make it stone by stone using a function:
def makePlafond(amount, initX, initY, initZ, name, floor, fuu, size,gname):
#fuu is not "fuu" is just a number for the floor
    n = str(name)
    f = str(floor)
    fu = str(fuu)
#for loop:
    for i in range(amount):
        # first row:
        s = str(i)
        # cmds.polyCylinder(n='p'+name+s)
        cmds.instance('deletePolyCylinder', n = 'p' + name +s)
        cmds.move( initX, initY, initZ + i * (size+0.1), f + n + s)
        cmds.xform(f + n + s, s = (size,3,size))
        cmds.rotate(0,0,'45deg', f+n+s)
        #add the obcjects inside the groups:
        cmds.parent(f+n+s,gname+ fu , relative=True )


#let's build some basic objs:
def buildBasicObj():
    cmds.polyCube(n = 'deletePolyCube')
    cmds.polyCube(n='deleteComplexPolyCube',sx=5, sy=5, sz=5)
    cmds.polyCube(n = 'deletePolyCylinder')
    cmds.polyCylinder(n='deleteComplexPolyCylinder', h=0.5)
    cmds.polyCylinder(n='deleteComplexPolyCylinderC', sx=12, sy=12, sz=5, h=3)
    cmds.polyCylinder(n='deleteComplexPolyCylinderD', sx=12, sy=12, sz=5, h=1.5)
    cmds.group('deletePolyCube', 'deleteComplexPolyCube','deletePolyCylinder','deleteComplexPolyCylinder', 'deleteComplexPolyCylinderC', 'deleteComplexPolyCylinderD', n = 'deleteGroup')


#let's make the buildTemple function:

def buildTemple():
    #call the function buildBasicObj:
    buildBasicObj()
    #call the function makeBase:
    makeBase()
    # slider variables:
    #amount of stages... more stages means less temple size.... min = 4, max... 12 ....
    floorStages = cmds.intSliderGrp("slider3", q=True, value=True)
    #don't touch anything below this line:
    initFloorS = floorStages + 1
    # let's make a loop with the function:
    makeGroup('floor',1)
    for i in range(1,4):
        makeGroup('column',i)
    #build the floor base:

    for i in range (len(cubeNames)):
        makeStonesP(floorStones,-30+i*3.1,-30,cubeNames[i],'a',1,3, 'floor')
    # floor stages:
    for i in range(1,floorStages):
        s = str(i)
        cmds.instance('floor1')
    for i in range(0, floorStages):
        cmds.move(0,i,0,'floor'+str(i+1))
    for i in range(0,floorStages):
        s = str(i+1)
        cmds.scale( 2 -i*0.1, 1, 2-i*0.1, 'floor'+s)
    
    #width of temple... here we go...............CRASH!!!!!!!!!!!!!!!!!-------------?????????
    templeWidth = cmds.intSliderGrp("slider1", q=True, value=True)
    #build the columns:
    for i in range(0,templeWidth):
        s = str(i)
        #first 6 columns:
        makeColumnsBase(i, 15 ,-17 ,columnNamesA[i]+s, 5, 'column', 1)
        #second 6s c:
        makeColumnsBase(i, 15 ,-17 ,columnNamesB[i]+s, 5, 'column', 2)
    #center columns:
    xmin, ymin, zmin, xmax, ymax, zmax = cmds.xform('column1', query=True, bb=True)
    totalCWidth = zmax - zmin
    #this loop will go out of range, I added more names in columnNamesC
    for i in range(1,11):
        s = str(i)
        # this 10 columns:
        makeColumnsBase(i, 13 , -17 ,columnNamesC[i]+s, 5, 'column', 3)
    #some adjustments over the groups:
    cmds.instance( 'column3' )

    #temple height variable:
    templeHeight = cmds.intSliderGrp("slider2", q=True, value=True)
    for i in range(1,5):
        s =  str(i)
        cmds.xform('column' + s, cp=1, s=(1.2,templeHeight,1.2))
        cmds.select('column'+s)
        cmds.move(9.75*templeHeight/2 + floorStages + floorStages/2, y=True, spr=True, ws=True)

    cmds.select('column1', 'column2')
    cmds.move(0,z=1, ws = True, spr=True)
    cmds.select('column3')
    cmds.move(0, totalCWidth,xz=True, ws = True, spr=True)
    cmds.rotate( 0, '90deg', 0, 'column3')
    cmds.select('column4')
    cmds.move(0,(-1)*totalCWidth,xz= True, ws = True, spr=True)
    cmds.rotate( 0, '90deg', 0, 'column4')

    cmds.setAttr('column1.translateX',14)
    cmds.setAttr('column2.translateX',-50)


    # build ceiling:

    cmds.polyCube(n='rc', w= 30)
    cmds.rotate(0,'180deg',0,'rc')
    cmds.scale(2.2,2,4, 'rc')
    cmds.move(0,16,-15,'rc')
    cmds.instance('rc')
    cmds.move(0,16,17,'rc1')
    cmds.instance('rc1')
    cmds.rotate(0,'90deg',0,'rc2')
    cmds.scale(1.2,2,4, 'rc2')
    cmds.move(33,16,1,'rc2')
    cmds.instance('rc2')
    cmds.move(-33,16,1,'rc3')

    makeGroup('minicolumn',1)
    for i in range(1,4):
        s = str(i)
        makeColumnsBase(i, 15 ,-17 ,columnNamesD[i]+s, 2, 'minicolumn', 1)

    cmds.scale(0.3,0.3,0.3,'minicolumn1')
    #cmds.move(-39,15.5,22,'minicolumn1')
    makeGroup('f_side',1)
    #cmds.parent('minicolumn1', 'f_side1' , relative=True)
    makeGroup('b_side',1)
    # let's try to loop this...
    for i in range(1,12):
        s = str(i)
        cmds.instance('minicolumn'+s)
        cmds.move(-39,15.5,22 - i*3,'minicolumn'+s)
        cmds.parent('minicolumn'+s, 'f_side1' , relative=True)

    for i in range(12,24):
        s = str(i)
        cmds.instance('minicolumn'+s)
        cmds.move(30,15.5,10 - i*3,'minicolumn'+s)
        cmds.parent('minicolumn'+s, 'b_side1' , relative=True)

    #small adjustments:
    cmds.move(0,0,1,'f_side1')
    cmds.move(0,0,47.5,'b_side1')

    #let's make the sides:
    makeGroup('miniside',1)

    for i in range(1,5):
        s = str(i)
        makeColumnsBase(i, 15 ,-17 ,columnNamesE[i]+s, 2, 'miniside', 1)

    cmds.scale(0.3,0.3,0.3,'miniside1')
    makeGroup('side', 1)
    for i in range(1,24):
        s = str(i)
        cmds.instance('miniside'+s)
        cmds.move(-39,15.5,19 - i*3,'miniside'+s)
        cmds.parent('miniside'+s, 'side1' , relative=True)
    cmds.rotate(0,'90deg',0,'side1')
    cmds.move(20.5,0,-16,'side1')
    cmds.instance('side1')
    cmds.move(20.5,0,-51,'side2')
    #let's make el "techo"
    cmds.polyCube(n='techo')
    cmds.move(0,18,1,'techo')
    cmds.scale(69,3,34, 'techo')
    cmds.instance('techo')
    cmds.scale(72,1,38, 'techo1')
    cmds.move(0,20.5,1,'techo1')
    cmds.instance('techo1')
    cmds.scale(68,1,19, 'techo2')
    cmds.move(0,22.5,-8,'techo2')
    cmds.instance('techo2')
    cmds.move(0,22.5,10,'techo3')
    cmds.rotate(16,0,0,'techo3')
    cmds.rotate(-16,0,0,'techo2')
    makeGroup('plafond',1)
    #build the floor base:
    for i in range (len(cubeNames)):
        makePlafond(20,-30+i*2.1,19,-30,cubeNames[i],'p',1,2, 'plafond')
    cmds.move(0,25,0,'plafond1')
    cmds.scale(1.5,0.1,0.4,'plafond1')
    cmds.rotate('16deg',0,0,'plafond1')
    cmds.move(16,20,14,'plafond1')
    cmds.instance('plafond1')
    cmds.rotate('-16deg',0,0,'plafond2')
    cmds.move(16,22.5,-4,'plafond2')
    #delete the unneeded assets and the bug:
    cmds.delete('deleteGroup', 'minicolumn24', 'miniside24')
    #let's make a big group and resize it according to the # of floors:
    cmds.group('rc','rc1','rc2','rc3','f_side1','b_side1','side1','side2', 'techo','techo1','techo2','techo3','plafond1','plafond2', n = 'temple')
    scaleRelative = (floorStages+1)/2
    #cmds.scale(scaleRelative,scaleRelative,scaleRelative,'temple')
    cmds.xform('temple', cp=1, s=(scaleRelative,scaleRelative,scaleRelative))
    totalCHeight = ymax - ymin
    cmds.select('temple')
    cmds.move(totalCHeight + totalCHeight/6, y= True,  ws = True, spr=True)
    cmds.rotate( 0, '90deg', 0, 'temple')

#there's a problem with the ceiling ,,,, we will fix later? thanks!

def fixPlafond():
    xmin, ymin, zmin, xmax, ymax, zmax = cmds.xform('column1', query=True, bb=True)
    totalCHeight = ymax - ymin
    cmds.select('temple')
    cmds.move(totalCHeight + totalCHeight/6, y= True,  ws = True, spr=True)

createWindow()










#let's block comment all these for the moment:
"""

#let's make a big group and resize it according to the # of floors:
cmds.group('column1', 'column2','column3','column4','rc','rc1','rc2','rc3','f_side1','b_side1','side1','side2', 'techo','techo1','techo2','techo3','plafond1','plafond2', n = 'temple')
scaleRelative = (floorStages / 2.5) * 0.2
cmds.scale(1.2 - scaleRelative,1.2 -scaleRelative,1.2 -scaleRelative,'temple')

#find the last # of floor and move the column groups in the top:

translateC = cmds.getAttr('floor'+ str(floorStages) +'.translateY')
realtranslate = translateC * 0.7 # 0.7 because it's 1.2 scale and 0.5 scale
cmds.select('temple')
cmds.move(0, translateC, 0, relative=False, objectSpace=True, worldSpaceDistance=True )


#cmds.memory(freeMemory=True megaByte=True asFloat=True sum=True) this doesn't work...
# run in MEL: ogs -gpu to check memory
"""
