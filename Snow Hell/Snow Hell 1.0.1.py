from gamelib import*

game = Game(960,540,"Snow Hell")

#Constant Objects----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#game parts
bk = Image("BK.png",game)
Moutain = Image("Moutain.png",game)
Skier1 = Image("Skier 1.png",game)
Skier2 = Image("Skier 2.png",game)
EP1 = Image("Finish.png",game)
EP2 = Image("Finish.png",game)
EP3 = Image("Finish.png",game)
T1 = Image("T1.png",game)
Blood = Image("Blood.png",game)
Explosion = Image("Explosion.png",game)
SExplo = Image("Snow Explosion.png",game)
VTS  = Image("VTS.png",game)
WS = Image("Win Screen.png",game)
CR = Image("Copyright.png",game)

#Game Title Screen Parts
title = Image("Logo.png",game)
tbk = Image("Title Screen.png",game)
start = Image("Start.png",game)
startL = Image("StartL.png",game)
howtoplay = Image("howtoplay.png",game)
howtoplayL = Image("howtoplayL.png",game)
HTWS = Image("HTWS.png",game)
PEX = Image("PEX.png",game)
story = Image("Story.png",game)

#Sound
Crash = Sound("Crash.wav",1)
TBlast = Sound("TNT Blast.wav",2)
SBlast = Sound("Snow Blast.wav",3)
Click = Sound("Click.wav",4)
BKM = Sound("BKM.wav",5)

#Count & Jump Variables----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping'''

M1 = 0#Make land ramp shape for Jump variable
osx = 0#1st Parameter
osy = 0#2nd Parameter
ga = 0#Game Over Count

#Changable Setttings------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Constant Variable
a = 64.21709517697867#Angle
s = 8#Speed
sb = 2.5#Speed Boost
m = 57/118#The Slope

#Font
f = Font(white,50,red,"Roboto Mono")# a Font object
fb = Font(white,30,red,"Roboto Mono")
flf = Font(magenta,50,white,"Roboto Mono")# a Font object
flfb = Font(magenta,30,white,"Roboto Mono")
lf = Font(magenta,40,white,"Roboto Mono")
fsx = 385
fsx2 = 355
fsx3 = 390
fsx4 = 283
fsy = 260
fsy2 = 340
lsx = 12
lsy = 510

#Base of Y-intercepts
TreeB = [-5,145,330]
RockB = [30,180,340]
T1B = [30,180,340]
VT1A = [60,199,370]

#Variables for LVL 1
TNA = 7 # of Trees
RNA = 7 # of Rocks
RA1 = 2000#Range 1st for A
RA2 = 10000#Range 2nd for A
REP1 = RA2+500#X-value of End Point
bksa = 3/4#Speed of Background LVL#1 Scroll

#Variables for LVL 2
TNB = 10 # of Trees
RNB = 10 # of Rocks
ENB = 10 # of TNT
RB1 = 2000#Range 1st for B
RB2 = 20000#Range 2nd for B
REP2 = RB2+500#X-value of End Point
bksb = 1#Speed of Background LVL#2 Scroll

#Variables for LVL 3
TNC = 13 # of Trees
RNC = 13 # of Rocks
ENC = 13 # of TNT
BNA = 7# of Blind Traps
RC1 = 2000#Range 1st for C
RC2 = 30000#Range 2nd for C
REP3 = RC2+500#X-value of End Point
bksc = 1.25#Speed of Background LVL#3 Scroll

#Starting Screen----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

title.y -= 150
title.resizeBy(50)
start.resizeBy(-40)
startL.resizeBy(-40)
howtoplay.resizeBy(-40)
howtoplay.y += 100
howtoplayL.resizeBy(-40)
howtoplayL.y += 100
#story.resizeBy(-40)
#story.y += 200
HTWS.visible = False
HTWS.resizeBy(-10)
PEX.visible = False
PEX.moveTo(760,470)
CR.resizeBy(-40)
CR.moveTo(800,520)

while not game.over:
    game.processInput()

    tbk.draw()
    title.draw()
    startL.draw()
    start.draw()
    howtoplay.draw()
    howtoplayL.draw()
    #story.draw()
    HTWS.draw()
    PEX.draw()
    BKM.play()
    CR.draw()

    if start.collidedWith(mouse):
        start.visible = False
        startL.visible = True
    else:
        start.visible = True
        startL.visible = False
        
    if howtoplay.collidedWith(mouse):
        howtoplay.visible = False
        howtoplayL.visible = True
    else:
        howtoplay.visible = True
        howtoplayL.visible = False

    if howtoplayL.collidedWith(mouse) and mouse.LeftClick :
        Click.play()
        HTWS.visible = True
        PEX.visible = True
    if howtoplayL.collidedWith(mouse) and mouse.LeftClick :
        Click.play()
        HTWS.visible = True
        PEX.visible = True
    if PEX.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        HTWS.visible = False
        PEX.visible = False
    
    if start.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        game.over = True

    if startL.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        game.over = True
    
    game.update(10)

game.over = False#continue the game with a new game loop

#Level 1 Game Loop---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Skier1.moveTo(950/2,270)
Skier1.rotateTo(-25)
Skier1.resizeTo(99,109)

Tree1 = []#empty list
for index in range(TNA):#use a loop to add items
    Tree1.append(Image("Tree.png",game))
for index in range(TNA):#use a loop to set the positions and speed
    x1 = randint(RA1,RA2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree1[index].moveTo(x1,y1)
    Tree1[index].setSpeed(s,a)
    Tree1[index].resizeBy(-60)

Rock1 = []#empty list
for index in range(RNA):#use a loop to add i6tems
    Rock1.append(Image("Rock.png",game))
for index in range(RNA):#use a loop to set the positions and speed
    x2 = randint(RA1,RA2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock1[index].moveTo(x2,y2)
    Rock1[index].setSpeed(s,a)
    Rock1[index].resizeBy(-50)

xep1 = REP1
yep1 = m*xep1+90
EP1.moveTo(xep1,yep1)
EP1.setSpeed(s,a)
EP1.resizeTo(512,598)
game.setBackground(bk)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksa)
    Moutain.draw()
    CR.draw()
    game.drawText("Level : 1",lsx,lsy,lf)

    for index in range(TNA):#the loop will go through the list of Tree
        Tree1[index].move()#each Tree will move
        if Tree1[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNA):#the loop will go through the list of Tree
        Rock1[index].move()#each Tree will move
        if Rock1[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    Skier1.draw()
    EP1.draw()
    EP1.move()
    
    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier1.x +=10
        Skier1.y -=5
        M1 -=5
        osx +=10
        osy -=5
    if keys.Pressed[K_LEFT] and osy <160:
        Skier1.x -=10
        Skier1.y +=5
        M1 +=5
        osx -=10
        osy +=5

#Jump-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    '''#Jump Keys

    if Skier1.y< 270+M1:
        landed = False#not landed
    else:
        landed = True

    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
        #Skier1.nextFrame()
        Skier1.y -=15*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .35:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
                  
    if not landed: #is jumping
         Skier1.y +=3#adjust for the height of the jump - lower number higher jump
           #Skier1.nextFrame()'''
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

    if EP1.isOffScreen("left"):
        game.drawText("You've Made It",fsx2,fsy,flf)
        game.drawText("Press Space to Continue to the Next Level",fsx4,fsy2,flfb)
        game.update()
        game.wait(K_SPACE)
        game.over = True
    
    game.update(60)

game.over = False

#Level 2 Game Loop------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s +=sb

Tree2 = []#empty list
for index in range(TNB):#use a loop to add items
    Tree2.append(Image("Tree.png",game))
for index in range(TNB):#use a loop to set the positions and speed
    x1 = randint(RB1,RB2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree2[index].moveTo(x1,y1)
    Tree2[index].setSpeed(s,a)
    Tree2[index].resizeBy(-60)

Rock2 = []#empty list
for index in range(RNB):#use a loop to add items
    Rock2.append(Image("Rock.png",game))
for index in range(RNB):#use a loop to set the positions and speed
    x2 = randint(RB1,RB2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock2[index].moveTo(x2,y2)
    Rock2[index].setSpeed(s,a)
    Rock2[index].resizeBy(-50)

T1 = []#empty list
for index in range(ENB):#use a loop to add items
    T1.append(Image("T1.png",game))
for index in range(ENB):#use a loop to set the positions and speed
    x3 = randint(RB1,RB2)
    b3 = T1B[randint(0,2)]
    y3 = m*x3+b3
    T1[index].moveTo(x3,y3)
    T1[index].setSpeed(s,a)
    T1[index].resizeBy(-75)

xep2 = REP2
yep2 = m*xep2+90
EP2.moveTo(xep2,yep2)
EP2.setSpeed(s,a)
EP2.resizeTo(512,598)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksb)
    Moutain.draw()
    CR.draw()
    game.drawText("Level : 2",lsx,lsy,lf)

    for index in range(TNB):#the loop will go through the list of Tree
        Tree2[index].move()#each Tree will move
        if Tree2[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNB):#the loop will go through the list of Tree
        Rock2[index].move()#each Tree will move
        if Rock2[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(ENB):#the loop will go through the list of Tree
        T1[index].move()#each Tree will move
        if T1[index].collidedWith(Skier1):
            TBlast.play()
            Explosion.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True

    Skier1.draw()
    EP2.draw()
    EP2.move()

    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier1.x +=10
        Skier1.y -=5
        M1 -=5
        osx +=10
        osy -=5
        
    if keys.Pressed[K_LEFT] and osy <160:
        Skier1.x -=10
        Skier1.y +=5
        M1 +=5
        osx -=10
        osy +=5

    if ga >0:
        game.over = True
        
    if EP2.isOffScreen("left"):
        game.drawText("You've Made It",fsx2,fsy,flf)
        game.drawText("Press Space to Continue to the Next Level",fsx4,fsy2,flfb) 
        game.update()
        game.wait(K_SPACE)
        game.over = True
    
    game.update(60)

game.over = False

#Level 3 Game Loop-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s +=sb

Tree3 = []#empty list
for index in range(TNC):#use a loop to add items
    Tree3.append(Image("Tree.png",game))
for index in range(TNC):#use a loop to set the positions and speed
    x1 = randint(RB1,RB2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree3[index].moveTo(x1,y1)
    Tree3[index].setSpeed(s,a)
    Tree3[index].resizeBy(-60)

Rock3 = []#empty list
for index in range(RNC):#use a loop to add items
    Rock3.append(Image("Rock.png",game))
for index in range(RNC):#use a loop to set the positions and speed
    x2 = randint(RB1,RB2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock3[index].moveTo(x2,y2)
    Rock3[index].setSpeed(s,a)
    Rock3[index].resizeBy(-50)

T2 = []#empty list
for index in range(ENC):#use a loop to add items
    T2.append(Image("T1.png",game))
for index in range(ENC):#use a loop to set the positions and speed
    x3 = randint(RB1,RB2)
    b3 = T1B[randint(0,2)]
    y3 = m*x3+b3
    T2[index].moveTo(x3,y3)
    T2[index].setSpeed(s,a)
    T2[index].resizeBy(-75)

VT1 = []#empty list
for index in range(BNA):#use a loop to add items
    VT1.append(Image("VT1.png",game))
for index in range(BNA):#use a loop to set the positions and speed
    x4 = randint(RB1,RB2)
    b4 = VT1A[randint(0,2)]
    y4 = m*x4+b4
    VT1[index].moveTo(x4,y4)
    VT1[index].setSpeed(s,a)
    VT1[index].resizeBy(-40)

xep2 = REP2
yep2 = m*xep2+90
EP2.moveTo(xep2,yep2)
EP2.setSpeed(s,a)
EP2.resizeTo(512,598)
VTS.moveTo(2000,2000)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksc)
    Moutain.draw()
    CR.draw()
    game.drawText("Level : 3",lsx,lsy,lf)

    for index in range(TNC):#the loop will go through the list of Tree
        Tree3[index].move()#each Tree will move
        if Tree3[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNC):#the loop will go through the list of Tree
        Rock3[index].move()#each Tree will move
        if Rock3[index].collidedWith(Skier1):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(ENC):#the loop will go through the list of Tree
        T2[index].move()#each Tree will move
        if T2[index].collidedWith(Skier1):
            TBlast.play()
            Explosion.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
      
    Skier1.draw()
    EP2.draw()
    EP2.move()
    
    for index in range(BNA):
        VT1[index].move()
        if VT1[index].collidedWith(Skier1):
            SBlast.play()
            #SExplo.moveTo(VT1[index].x,VT1[index].y)
            SExplo.visible = True
            SExplo.draw()
            VTS.moveTo(940/2,540/2)
            VTS.setSpeed(0,0)
            game.time=3
    
    VTS.draw()
    
    if game.time<1:
        VTS.setSpeed(5,180)
        VTS.move()
        SExplo.visible = False
        
    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier1.x +=10
        Skier1.y -=5
        M1 -=5
        osx +=10
        osy -=5
        
    if keys.Pressed[K_LEFT] and osy <160:
        Skier1.x -=10
        Skier1.y +=5
        M1 +=5
        osx -=10
        osy +=5

    if ga >0:
        game.over = True
    
    if EP2.isOffScreen("left"):
        WS.draw()
        game.update()
        game.wait(K_SPACE)
        game.over = True
    
    game.update(60)

game.over = False

game.quit() 

