from pygame import*
from math import *
from random import *

init()      #initialize

size = width, height = 1000, 700    #set the size of the screen
screen = display.set_mode(size)     #set the screen 

#set  colours
BLACK = (0, 0, 0) 
DARKGREY = (70,70,70)
GREY = (197, 209, 207)
RED = (255, 0, 0)
BLUE = (79, 146, 255)
WHITE = (255,255,255)
YELLOW = (247,234, 93)
PINK = (255, 168, 142)
PURPLE = (219, 76, 255)
GREEN = (116, 211, 42)
 
CYAN = (149, 171, 194)

#set fonts
font1 = font.SysFont("Calibri",30)
font2 = font.SysFont("Calibri",40)
font3 = font.SysFont("Calibri",50)
fontTreL = font.SysFont("trebuchetms", 50)
fontTreM = font.SysFont("trebuchetms", 35)
fontTreS = font.SysFont("trebuchetms", 24)
fontTreS2 = font.SysFont("trebuchetms", 20)
fontTreXs = font.SysFont("trebuchetms", 17)
fontCon = font.SysFont("consolas",24,italic=True)

#define the states

EXITSTATE = 1
EXPLAINSTATE = 0
HOMESTATE = 3
MAINSTATE = 4
GAMESTATE = 5
RULESTATE = 6
STORESTATE = 7
DONESTATE = 8
FREESTATE = 9
INFORMSTATE = 10
INVSTATE=11

#load images
bossPic = image.load("images/Boss.png")
bubblePic = image.load("images/bubble.jpeg")
angryBoss = image.load("images/angryBoss.png")
happyBoss = image.load("images/happyBoss.png")
wings = image.load("images/wing.png")
portal = image.load("images/portal1.png")
portal = transform.scale(portal, (80,80))
portal2 = image.load("images/portal2.png")
portal2 = transform.scale(portal2,(80,80))
pill = image.load("images/pill.png")
android = image.load("images/android.png")
leg1= image.load("images/legs1.jpg")
leg2= image.load("images/legs2.jpg")
helpPic = image.load("images/help.png")
backpackPic = image.load("images/backpack.png")
shopPic = image.load("images/shop.png")
flagPic = image.load("images/flag.png")
computerPic = image.load("images/computer.png")
debugPic = image.load("images/debug.png")
potion1Pic = image.load("images/potion1.png")
potion2Pic = image.load("images/potion2.png")
virusPic = image.load("images/virus.png")
trapPic = image.load("images/trap.png")
moneyBagPic = image.load("images/moneyBag.png")
bombPic = image.load("images/bomb.png")
timeBombPic = image.load("images/timeBomb.png")
rulePic = image.load("images/rule.png")

def drawArrow (x,y):
    draw.rect (screen, CYAN, (x,y,48,34))
    draw.rect (screen, WHITE, (x+10,y+10,15,14))
    draw.polygon (screen, WHITE, ((x+25,y+5),(x+25,y+29),(x+40,y+17)))

def explain(button,mx,my):  #explain the scenario to the user
    global inputing, entered

    level = [1,1]
    money = 300             #set default money
    itemList = [0,0,0,1]    #no items

    state=EXPLAINSTATE      
    draw.rect(screen, WHITE, (0, 0, width, 2*height//3))     #draw background
    draw.rect(screen, GREY, (0, 2*height//3, width, height//3)) 
    screen.blit(bossPic,(100,270))      #draw the boss
    screen.blit(transform.scale(bubblePic, (640,330)), (270,30))
    drawArrow (780,548) 
    nextRect = Rect (780, 548, 48, 34)

    #write the scenario
    screen.blit(fontTreS.render("We are in an emergency!", 1, BLACK), (450,110,100,100))
    screen.blit(fontTreS.render("An anonymous group is trying to hack our", 1, BLACK), (350,150,100,100))
    screen.blit(fontTreS.render("company. As a cyber security specialist, you", 1, BLACK), (350,190,100,100))
    screen.blit(fontTreS.render("need to protect our documents.", 1, BLACK), (450,230,100,100))
    
    #write the command
    string = "Enter your name to continue:"
    text = fontTreS.render(string, 1, BLACK)
    textSize = fontTreS.size(string)
    textRect = Rect(100, 550, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #draw the box where user writes their name
    inputRect = draw.rect(screen, WHITE, (110+textSize[0], 548, 330, 35))
    
    #display the username
    string=username
    writeRect=Rect(118+textSize[0],550,400,50)
    text = fontTreS.render(string, 1, BLACK)
    screen.blit(text, writeRect)
    if entered == True:
        state = HOMESTATE
        entered = False
    if inputing == True:
        draw.rect(screen, CYAN,inputRect,2)
    if len(username)>=1:
        #user must type their username before starting a game
        if nextRect.collidepoint(mx,my) == True:
            state=HOMESTATE  
    if button == 1:
        if inputRect.collidepoint(mx,my)==True:
            inputing = True 
    return state, level, money, itemList

def drawBack ():
    string = "BACK"
    text = fontTreS2.render(string, 1, BLACK)
    fontSize = fontTreS2.size(string)
    backRect = draw.rect(screen, GREY, (width-75,0,80,37))
    screen.blit(text, Rect(width-60, 7, fontSize[0],fontSize[1])) 

def drawBox (x,y):
    #draw a white framed box in shop
    box = Rect (x,y,300,250)
    draw.rect(screen,WHITE,box,4)
    draw.rect(screen,WHITE, (x,y+205,300,45))

def drawStore (button,mx,my,buttonList,infoList,money,purchaseMsg,infoMsg,itemList):
    #draw an item store
    state = STORESTATE
    draw.rect(screen, BLACK, (0, 0, width, height))
    
    #back button
    backRect = Rect(width-75,0,80,37)
    drawBack()  
    
    #write the user's balance
    string = "$"+str(money)
    text = fontTreM.render(string, 1, YELLOW)
    screen.blit(text, Rect(40, 27, 100, 100))  
    
    #draw boxes
    drawBox(150,90)
    drawBox(550,90)
    drawBox(150,390)
    drawBox(550,390)

    #draw images of the items
    screen.blit(transform.scale(wings, (240,125)), (177,135))
    screen.blit(transform.scale(debugPic, (114,114)),(645,155))
    screen.blit(transform.scale(potion1Pic,(130,150)), (242,438))
    screen.blit(transform.scale(potion2Pic,(130,150)), (637,438))
    
    buttonList = buttonList[:4]     #take only the first four items
    infoList = infoList[:4]         #take only the first four items

    if button==1:           #info of the items and purchase message
        for x in range (0,4):
            if buttonList[x].collidepoint(mx,my) == True:
                #write that the user has purchased the item 
                infoMsg =""
                if x == 0:
                    if money>=800:          #wings
                        money-=800  
                        purchaseMsg = "Wings purchased."
                        itemList[3] += 1
                    else:
                        purchaseMsg = "Not enough money."
                elif x == 1:
                    if money>=360:          #debugger
                        money-=360  
                        purchaseMsg = "Debugger purchased."
                        itemList[2] += 1 
                    else:
                        purchaseMsg = "Not enough money."
                elif x == 2:        
                    if money>=100:          #elixir of health
                        money-=100  
                        purchaseMsg = "Elixir of health purchased."
                        itemList[0] += 5  
                    else:
                        purchaseMsg = "Not enough money."
                else:
                    if money>=150:          #potion of strength
                        money-=150  
                        purchaseMsg = "Potion of strength purchased." 
                        itemList[1] += 2    
                    else:
                        purchaseMsg = "Not enough money."
        for x in range (0,4):
            if infoList[x].collidepoint(mx,my) == True:
                purchaseMsg=""
                #write the function of each item when their name is clicked. 
                if x == 0:
                    infoMsg = "Your speed increases."          #write the wings' skill
                elif x == 1:
                    infoMsg = "The debugger gets rid of one purple trap virus. (Q)"       #write the debugger's skill
                elif x == 2:
                    infoMsg = "The elixir heals your health. (W)"    #write the elixir's skill
                else:
                    infoMsg = "The potion gets rid of 3 blue viruses. (E)"       #write the potion's skill
        if backRect.collidepoint(mx,my) == True:
            state = HOMESTATE 
                        
    text = fontTreS.render(purchaseMsg, 1, YELLOW)
    textSize = fontTreS.size(purchaseMsg)
    screen.blit(text, Rect(width//2-textSize[0]//2, 32, textSize[0], textSize[1])) 

    text = fontTreS.render(infoMsg, 1, YELLOW)
    textSize = fontTreS.size(infoMsg)
    screen.blit(text, Rect(width//2-textSize[0]//2, 32, 100, 40))  

    #write the name and price of the item  
    writePrice (800,"Wings",73,283,76,85,78)
    writePrice (360,"Debugger",473,283,460,85,480)
    writePrice (100,"Elixir of life",73,583,45,385,78)
    writePrice (150,"Potion of strength",473,583,412,385,480)
        
    return state, money, purchaseMsg, infoMsg, itemList

def writePrice (x,y,a,b,c,d,e):
    #write the price (x) with how much it is shifted (a,b)
    string = "$"+str(x)
    text = fontTreS.render(string, 1, BLACK)
    screen.blit(text, Rect(190+e, b+20, 100, 100))
    
    #write the name (y) with how much it is shifted (c,d)
    string = y
    text = fontTreS.render(string, 1, WHITE)
    textRect = Rect(190+c, d+15, 100,100)
    screen.blit(text, textRect)
    
    #draw a buy button
    buyRect = Rect(90+a, b+20, 55, 30)
    draw.rect(screen,GREY, buyRect)
    string = "BUY"
    text = fontTreS.render(string, 1, BLACK)
    screen.blit(text, Rect(95+a, b+20, 100, 100)) 
    
    #draw an info circle
    infoCircle = draw.circle(screen,GREY, (350+a,b+35),15)
    string = "i"
    text = fontCon.render(string, 1, BLACK)
    screen.blit(text, Rect(344+a, b+25, 100, 100))

    #add the rectangle to the list
    buttonList.append (buyRect)
    infoList.append(infoCircle)
   
    return buttonList, infoList

def mainHome (button,mx,my,speed):
    state=HOMESTATE  
    draw.rect(screen, GREY, (0, 0, width, height)) 
    stage = 1
    freePlay = False
    circleX=[]
    circleY=[]
    circleX2=[]
    circleY2=[]            
    numKilled = 0
    numBlue = 0
    radius = 20
    barHeight = 0
    locationX = 500
    locationY = 700  
    
    screen.blit(transform.scale(flagPic, (120,120)),(270,200))
    text = fontTreXs.render("Virus Slayer", 1, BLACK)
    screen.blit(text, Rect(292, 325, 100, 100))
    playRect = Rect(270,200,120,120)

    screen.blit(transform.scale(computerPic, (120,120)),(440,200))
    text = fontTreXs.render("Free Play", 1, BLACK)
    screen.blit(text, Rect(465, 325, 100, 100))
    freeRect =Rect(440,200,120,120)

    screen.blit(transform.scale(timeBombPic, (100,100)),(615,210))
    text = fontTreXs.render("Time Bomb", 1, BLACK)
    screen.blit(text, Rect(634, 325, 100, 100))
    timeBombRect = Rect(615,200,120,120)

    screen.blit(transform.scale(backpackPic, (120,120)),(270,400))
    text = fontTreXs.render("Inventory", 1, BLACK)
    screen.blit(text, Rect(297, 530, 100, 100))
    inventoryRect = Rect (270,400,120,120)

    screen.blit(transform.scale(shopPic, (120,120)),(440,400))
    text = fontTreXs.render("Shop", 1, BLACK)
    screen.blit(text, Rect(478, 530, 100, 100))
    storeRect = Rect(440,400,120,120)

    screen.blit(transform.scale(helpPic, (120,120)),(610,400))
    text = fontTreXs.render("Help", 1, BLACK)
    screen.blit(text, Rect(655, 530, 100, 100))
    helpRect = Rect(620,400,120,120)

    if button==1:
        if playRect.collidepoint(mx,my) == True:
            #if the play button is clicked, change to the main screen
            state = MAINSTATE   
            stage = 1
            freePlay = False
        if freeRect.collidepoint(mx,my) == True:
            #if the free play button is clicked, change to the game screen
            state = GAMESTATE  
            #reset variables for a new freeplay game
            freePlay = True 
            circleX=[]
            circleY=[]
            circleX2=[]
            circleY2=[]            
            numKilled = 0
            numBlue = 0
            radius = 20
            barHeight = 0
            locationX = 500
            locationY = 700 
            speed = 3
        if storeRect.collidepoint(mx,my) == True:
            state = STORESTATE    
        if helpRect.collidepoint(mx,my) == True:
            state = RULESTATE           
        if inventoryRect.collidepoint(mx,my) == True:
            state = INVSTATE
        if timeBombRect.collidepoint(mx,my) == True:
            state = MAINSTATE   
            stage = 2
            freePlay = False
            
    return state,stage, freePlay,circleX,circleY,circleX2,circleY2,numKilled,numBlue,radius,barHeight,locationX,locationY,speed

def mainMenu (button,mx,my):
    state = MAINSTATE     
    gameStartTime = 0
    numKilled = 0
    circleX=[]
    circleY=[]
    circleX2=[]
    circleY2=[] 
    circleX3=[]
    circleY3=[]    
    numBlue = 0   
    radius = 20
    barHeight = 0
    locationX = 500
    locationY = 700
    portalX = []
    portalY = []
    portalX2 = []
    portalY2 = []
    wingUsed = False
    draw.rect(screen, GREY, (0, 0, width, height))     #draw background
    
    string = "BACK"
    text = fontTreS2.render(string, 1, BLACK)
    fontSize = fontTreS2.size(string)
    backRect = draw.rect(screen, CYAN, (width-75,0,80,37))
    screen.blit(text, Rect(width-60, 7, fontSize[0],fontSize[1])) 

    string = "# Successive Wins: %i" %(failList.count("1"))
    text = fontTreS.render(string, 1, BLACK)
    fontSize = fontTreS.size(string)
    screen.blit(text, Rect(width//2-fontSize[0]//2, 150, fontSize[0],fontSize[1])) 
    if stage ==1:
        #write the rules for the specific level and stage 
        levelText = str(level[0]) 
        stageText = "VIRUS SLAYER"
        for j in range (1,6):
            if level[0] == j:
                ruleText = "Get rid of %i viruses." %(40+15*(j-1))
    else:
        stageText = "TIME BOMB"
        levelText = str(level[1]) 
        if level[0] == 1:
            ruleText = "Get rid of 15 viruses in 30 seconds."
        elif level[0] == 2:
            ruleText = "Get rid of 20 viruses in 30 seconds."
        elif level[0] == 3:
            ruleText = "Get rid of 30 viruses in 30 seconds."
        elif level[0] == 4:
            ruleText = "Get rid of 35 viruses in 45 seconds."
        else:
            ruleText = "Get rid of 45 viruses in 45 seconds."

    text = fontTreM.render(ruleText, 1, BLACK)
    textSize = fontTreM.size(ruleText)
    screen.blit(text, Rect(width//2-textSize[0]//2, 300, 100, 100))    
        
    #write the level and stage
    string = str(stageText)
    text = fontTreL.render(string, 1, BLACK)
    fontSize = fontTreL.size(string)
    screen.blit(text, Rect(width//2-fontSize[0]//2, 40, 100, 100))
    string = "level: " + levelText
    text = fontTreS.render(string, 1, BLACK)
    fontSize = fontTreS.size(string)
    screen.blit(text, Rect(width//2-fontSize[0]//2, 110, 100, 100))
    
    #draw&write the start option
    startRect = Rect(width//2-100, 380, 200, 50) 
    draw.rect(screen, CYAN, startRect)
    string = "START"
    text = fontTreM.render(string, 1, BLACK)
    screen.blit(text, Rect(448, 385, 100, 100)) 
        
    if button==1:
        if startRect.collidepoint(mx,my)==True:
            state = GAMESTATE
            #reset variables for the next game
            circleX=[]
            circleY=[]
            circleX2=[]
            circleY2=[]    
            circleX3=[]
            circleY3=[]         
            numKilled = 0
            numBlue = 0
            gameStartTime = time.get_ticks()
            radius = 20
            barHeight = 0
            locationX = 500
            locationY = 700 
            portalX = []
            portalY = []
            portalX2 = []
            portalY2 = []  
            wingUsed = False
        if backRect.collidepoint(mx,my) == True:
            state = HOMESTATE
        
    return state,gameStartTime,circleX,circleY,numKilled,circleX2,circleY2,numBlue,radius,barHeight,locationX,locationY,portalX,portalY,portalX2,portalY2,wingUsed

def writeRule (button,mx,my):
    #inform the user about the rules
    state = RULESTATE
    draw.rect(screen, WHITE, (0, 0, width, height))      

    screen.blit(rulePic,(0,0))
    
    #back button
    string = "BACK"
    text = fontTreS2.render(string, 1, BLACK)
    fontSize = fontTreS2.size(string)
    backRect = draw.rect(screen, CYAN, (width-75,0,80,37))
    screen.blit(text, Rect(width-60, 7, fontSize[0],fontSize[1])) 
        
    if backRect.collidepoint(mx,my) == True:
        state=HOMESTATE  
        
    return state

def playGame (button,locationX,locationY,radius,killPurple,killBlue,healthRecover,itemList,speed,wingUsed):
    #free play state
    global barHeight, startTimer
    state = GAMESTATE  
    #print(itemList)
    #print(speed)
    failed=False
    ranNum = 0
    anotherNum = 0
    purpleHit = False
    draw.rect(screen, BLACK, (0, 0, width, height)) 
    draw.line(screen,WHITE,(925,0),(925,800),2)     
    draw.rect(screen,WHITE,(940,20,45,350),3)       #draw a health bar
    draw.rect(screen,CYAN,(943,22,42,347))          #health bar filled
    draw.rect(screen,BLACK,(943,22,42,barHeight))   #health decrease bar
    
    draw.line(screen,WHITE,(925,385),(1000,385),3)

    screen.blit(transform.scale(potion1Pic,(51,59)),(938,390))
    screen.blit(transform.scale(potion2Pic,(51,59)),(938,480))
    screen.blit(transform.scale(debugPic,(43,43)),(940,572))
    
    
    text = fontTreXs.render("%i (W)" %itemList[0], 1, WHITE)
    screen.blit(text, Rect(949, 450, 100, 100))  

    text = fontTreXs.render("%i (E)" %itemList[1], 1, WHITE)
    screen.blit(text, Rect(949, 540, 100, 100))  

    text = fontTreXs.render("%i (Q)" %itemList[2], 1, WHITE)
    screen.blit(text, Rect(949, 621, 100, 100))  

    #write the number of viruses killed
    draw.line(screen,WHITE,(925,652),(1000,652),3)
    numKilled=numBlue-len(circleX)  #calculate the number of viruses that the user got rid of
    string = str(numKilled)
    text = fontTreS.render(string, 1, WHITE)
    screen.blit(text, Rect(947, 660, 100, 100))   

    if itemList[3] > 0:     #if the user has a wing item
        wingUsed = True  
        itemList[3] -= 1
    if wingUsed == True:
        #increase the speed if the wing is used
        speed += 1
        realWings = transform.scale (wings,(3*round(radius),3*round(radius)//2))  #draw wings to the android
        screen.blit(realWings,(locationX-round(radius)//2,locationY))
        wingUsed = False

    if time.get_ticks()-startTimer>=2000:       #health bar decreases at a dif rate depending on the #viruses
        if 10>len(circleX)>=6:
            barHeight+=0.17
        elif 13>len(circleX)>=10:
            barHeight+=0.2
        elif 16>len(circleX)>=13:
            barHeight+=0.25
        elif len(circleX)>=16:
            barHeight+=0.3
            
    #items
    if killPurple == True:
        itemList[2] -= 1        #subtract one from the list 
        killPurple = False      #set the variable to false again 
        if len(circleX2) > 0:
            #check if there is more than one purple virus
            ranNum = randint(0,len(circleX2)-1) #get a random number
            #get rid of a random purple virus
            del circleX2[ranNum]
            del circleY2[ranNum]

    if killBlue == True:
        itemList[1] -= 1        #subtract one from the list 
        killBlue = False
        
        if len(circleX) > 3:
            for i in range (0,3):
                deleteBlueNum = randint(0,len(circleX)-1)  
                del circleX[deleteBlueNum]
                del circleY[deleteBlueNum]
        else:
            for j in range (0,len(circleX)):
                deleteBlueNum1 = randint(0,len(circleX)-1)  
                del circleX[deleteBlueNum1]
                del circleY[deleteBlueNum1]
            
    if healthRecover == True:
        itemList[0] -= 1
        healthRecover = False          
        if barHeight > 0:      
            barHeight -= 25

    #blue viruses
    x=0
    while x<len(circleX):       
        screen.blit(transform.scale(virusPic,(32,32)), (circleX[x],circleY[x]))
        distance = sqrt((circleX[x]+15-locationX-radius)**2+(circleY[x]+15-locationY-radius)**2)

        if distance < radius+15:  #sum of the radii's            
            #get rid of the collided virus's coordinates from lists
            del circleX[x]  
            del circleY[x]
            radius+=0.7   #makes the size of the android larger
        x+=1
    
    #purple traps
    for b in range (0,len(circleX2)):   
        screen.blit(transform.scale(trapPic,(59,59)), (circleX2[b],circleY2[b]))   #draw purple trap viruses
        distance = sqrt((circleX2[b]+29-locationX-radius)**2+(circleY2[b]+29-locationY-radius)**2)
        if distance < radius+20:    #sum of the radii's 
            purpleHit = True

    if purpleHit == True:       #effect when purple traps are hit
        barHeight+=0.6          #decreases health
        if speed > 2.2:
            speed -= 0.05 
        purpleHit = False  

    #health pill      
    if len(circleX3)>0:
        screen.blit(transform.scale(pill,(30,30)),(circleX3[-1],circleY3[-1]))     
        pillDistance = sqrt((circleX3[-1]+14-locationX-radius)**2+(circleY3[-1]+14-locationY-radius)**2)
    
        if pillDistance < radius+18:    #sum of the radius and the pill image
            radius -= 7.5               #decrease the radius by 7
            del circleX3[-1]
            del circleY3[-1]                    

        if time.get_ticks()-drawTime>3500:
            del circleX3[-1]
            del circleY3[-1]  
     
    #portal
    x = 0 
    while x < len(portalX): 
        portalCircle = draw.circle(screen,BLACK, (portalX[x]+40,portalY[x]+40),34)
        screen.blit(portal,(portalX[x],portalY[x]))     #draw an enter portal
        screen.blit(portal2,(portalX2[x],portalY2[x]))  #draw an exit portal
        
        if portalCircle.collidepoint(round(locationX+radius),round(locationY+radius)) == True:
            #change the location to the exit portal
            locationX = portalX2[x] + radius
            locationY = portalY2[x]
            
            #get rid of the portals from the list
            del portalX[x]      #enter portal
            del portalY[x]            
            del portalX2[x]     #exit portal
            del portalY2[x]
        x+=1    
    
    if barHeight>=344:
            state = DONESTATE   #the game finishes when the health is zero
    
    if freePlay==True:
        #bomb
        for i in range (0,len(bombList)//2):
            screen.blit(transform.scale(bombPic,(70,70)),(bombList[0],bombList[1]))
            bombDistance = sqrt((bombList[0]+17-locationX-radius)**2+(bombList[1]+17-locationY-radius)**2)
            if bombDistance < radius+20:
                state=DONESTATE
                bombList.clear()
            if time.get_ticks()-drawTime2 > 6000:
                bombList.clear()
    
    else:
        if barHeight>=344:
            failed = True
        
        #bomb
        for i in range (0,len(bombList)//2):
            screen.blit(transform.scale(bombPic,(70,70)),(bombList[0],bombList[1]))
            bombDistance = sqrt((bombList[0]+17-locationX-radius)**2+(bombList[1]+17-locationY-radius)**2)
            if bombDistance < radius+20:
                failed = True
                bombList.clear()
                state=DONESTATE
            if time.get_ticks()-drawTime2 > 6000:
                bombList.clear()

        if stage == 1:
            for i in range (1,6):
                if level[0] == i and numKilled>=(40+15*(i-1)):
                    state = DONESTATE

        if stage == 2:
            #write the time
            if len(str(time.get_ticks() - gameStartTime))<4:
                a = "00" + str(time.get_ticks() - gameStartTime)
            elif len(str(time.get_ticks() - gameStartTime))<5:
                a = "0"+str(time.get_ticks() - gameStartTime)
            else:
                a = str(time.get_ticks() - gameStartTime)
                
            string = a[:2] +":"+ a[2:4]     #make it into a time format (e.g. 1230 into 12:30) 
            text = fontTreS2.render(string, 1, WHITE)
            screen.blit(text, Rect(10, 10, 100, 100)) 
            
            if level[1] == 1 or level[1] == 2 or level[1] == 3:  
                if time.get_ticks()-gameStartTime>30000:
                    if level[1] == 1:
                        if numKilled>=15:
                            #stage two, level one ends when more than 30 viruses are killed in 45 seconds
                            state = DONESTATE
                        else:
                            state = DONESTATE           
                            failed=True         #fail when not enough viruses were killed.                    
                    elif level[1] == 2:
                        if numKilled>=20:
                            #stage two, level two ends when more than 40 viruses are killed in 45 seconds
                            state = DONESTATE
                        else:
                            state = DONESTATE           
                            failed=True         #fail when not enough viruses were killed.
                    elif level[1] == 3:
                        if numKilled>=30:
                            #stage two, level one ends when more than 30 viruses are killed in 45 seconds
                            state = DONESTATE
                        else:
                            state = DONESTATE           
                            failed=True         #fail when not enough viruses were killed.
            else:
                if time.get_ticks()-gameStartTime>45000:                    
                    if level[1] == 4:
                        if numKilled>=35:
                            #stage two, level two ends when more than 40 viruses are killed in 45 seconds
                            state = DONESTATE
                        else:
                            state = DONESTATE           
                            failed=True
                    elif level[1] == 5:
                        if numKilled>=45:
                            #stage two, level two ends when more than 40 viruses are killed in 45 seconds
                            state = DONESTATE
                        else:
                            state = DONESTATE           
                            failed=True 
            
    return state,failed, radius, locationX,locationY,killPurple,killBlue,healthRecover,itemList,numKilled,speed,wingUsed

def drawInv (button,mx,my):
    state = INVSTATE
    draw.rect(screen, BLACK, (0, 0, width, height))

    drawBack()
    backRect = Rect(900, 0, 100, 50) 
    string="%s's Inventory" %username
    fontSize = fontTreM.size(string)
    text = fontTreM.render(string, 1, WHITE)
    screen.blit(text, Rect(width//2-fontSize[0]//2, 60, 70, 100))

    string="$ %i" %money 
    text = fontTreS.render(string, 1, YELLOW)
    screen.blit(text, Rect(width//2-fontSize[0]//2-240, 68, 70, 100))

    #draw the items
    screen.blit(transform.scale(wings, (260,135)), (374,230))
    screen.blit(transform.scale(debugPic, (95,95)),(230,455))
    screen.blit(transform.scale(potion1Pic,(90,110)), (455,450))
    screen.blit(transform.scale(potion2Pic,(90,110)), (680,450))

    string="Elixir of Health: %i" %itemList[0] 
    text = fontTreS2.render(string, 1, WHITE)
    screen.blit(text, Rect(423, 570, 70, 100))

    string="Potion of Strength: %i" %itemList[1]
    text = fontTreS2.render(string, 1, WHITE)
    screen.blit(text, Rect(640, 570, 70, 100))

    string="Debugger: %i" %itemList[2]
    text = fontTreS2.render(string, 1, WHITE)
    screen.blit(text, Rect(220, 570, 70, 100))

    string="Wings: %i" %itemList[3]
    text = fontTreS2.render(string, 1, WHITE)
    screen.blit(text, Rect(464, 385, 70, 100))

    if button==1:
        if backRect.collidepoint(mx,my) == True:
            state = HOMESTATE

    return state

def doneGame (button,mx,my,money):               
    #shows score
    global failList, circleX, circleY,circleX2,circleY2,numKilled, numBlue, radius, barHeight, locationX, locationY, speed, level,failed, stageLevel
    state = DONESTATE  
    gameOver = False
    levelUp = False   
    speed = 3 
    draw.rect(screen, GREY, (0, 0, width, height))
    nextRect = Rect(width//2-80,400,160,52)

    if stage == 1:
        stageLevel = level[0]
    else:
        stageLevel = level[1]
    if freePlay == True:
        #show how many viruses the user has killed if it is free play
        fontSize = fontTreL.size("GAME OVER")
        text = fontTreL.render("GAME OVER", 1, BLACK)
        screen.blit(text, Rect(width//2-fontSize[0]//2, 100, 100, 100))

        #show how many viruses the user has killed if it is free play
        string = "score : " + str(numKilled)
        fontSize = fontTreM.size(string)
        text = fontTreM.render(string, 1, BLACK)
        screen.blit(text, Rect(width//2-fontSize[0]//2, 170, 100, 100))

        #money
        screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
        text=fontTreM.render("+ $%i" %numKilled,1,BLACK)
        screen.blit(text, Rect(510, 270, 100, 100))

        #go to home button
        backRect = draw.rect(screen,CYAN,(180,420,280,60)) 
        text = fontTreM.render("Back to Main", 1, BLACK)
        textRect = Rect(220, 430, 100,100)
        screen.blit(text, textRect)   

        #play again button
        againRect=draw.rect(screen, CYAN,(width-480,420,280,60))
        text = fontTreM.render("Play Again", 1, BLACK)
        textRect = Rect(width-420, 430, 100,100)
        screen.blit(text, textRect)  

    else:
        nextRect = draw.rect(screen,CYAN, (width//2-80,400,160,52))
        string = "Next"
        fontSize = fontTreM.size(string)
        text = fontTreM.render(string, 1, BLACK)
        screen.blit(text, Rect(width//2-fontSize[0]//2, 405, 100, 100))
        if failed == True:      #when the user fails
            screen.blit(transform.scale(angryBoss, (180,180)), (100,200))
            string = "Mission Failed"
            fontSize = fontTreM.size(string)
            text = fontTreM.render(string, 1, BLACK)
            screen.blit(text, Rect(width//2-fontSize[0]//2, 170, 100, 100))
  
            if stageLevel<5:
                #lose money
                screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
                text=fontTreM.render("- $%i" %100*stageLevel,1,BLACK)
                screen.blit(text, Rect(510, 270, 100, 100))
        elif failed == False:   #when the user succeeds
            screen.blit(transform.scale(happyBoss, (180,180)), (100,200))       #display a happy boss image
            
            string = "Mission Completed"
            fontSize = fontTreM.size(string)
            text = fontTreM.render(string, 1, BLACK)
            screen.blit(text, Rect(width//2-fontSize[0]//2, 170, 100, 100))

            if stageLevel<5:
                #earn money
                screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
                text=fontTreM.render("+ $%i" %(100*stageLevel),1,BLACK)
                screen.blit(text, Rect(510, 270, 100, 100))

            else:
                #go to home button
                backRect = draw.rect(screen,CYAN,(width//2-140,420,280,60)) 
                text = fontTreM.render("Back to Main", 1, BLACK)
                fontSize = fontTreM.size("Back to Main")
                textRect = Rect(width//2-fontSize[0]//2, 430, 100,100)
                screen.blit(text, textRect)  
                
    if button == 1:
        if freePlay == True:
            if backRect.collidepoint(mx,my) == True:
                state = HOMESTATE
                money+=numKilled
            if againRect.collidepoint(mx,my) == True:
                if freePlay == True:
                    money+=numKilled
                    state = GAMESTATE
                    circleX=[]
                    circleY=[]
                    circleX2=[]
                    circleY2=[]            
                    numKilled = 0
                    numBlue = 0
                    radius = 20
                    barHeight = 0
                    locationX = 500
                    locationY = 700 
                    speed = 3
        else:
            if nextRect.collidepoint(mx,my) == True:
                if failed ==True:
                    if failList[-1] != "0":            
                        failList=[]  
                    failList.append("0")
                    money-=100*stageLevel
                else:
                    money+=100*stageLevel
                    if failList[-1] != "1":            
                        failList=[]
                    failList.append ("1")       
                if len(failList) == 3:
                    state = INFORMSTATE
                    if failList[0]=="1":        #level up if there are three consecutive successes
                        levelUp = True
                    else:
                        gameOver = True         #game over if there are three consecutive losses
                else:
                    state = MAINSTATE
                 
    return state,stage,money,gameOver,levelUp, speed

def informUser (button,mx,my,level,speed,money,itemList,failList):
    #inform the user about game over or level up
    state = INFORMSTATE     #define the state
    draw.rect (screen,GREY,(0,0,width,height))     #draw the background
    
    nextRect = Rect (width//2-110,440,220,50)

    #draw&write a button to go back to the main screen
    newRect=draw.rect(screen,CYAN,(width//2-110,515,220,50))
    string="Back to Main"
    text = fontTreS.render(string, 1, BLACK)
    fontSize = fontTreS.size(string)
    textRect = Rect(width//2-fontSize[0]//2, 525, 100,100)
    screen.blit(text, textRect)

    if gameOver == True:
        #if it is game over, draw a note that is decreasing in size
        string = "YOU ARE FIRED!"
        fontSize = fontTreM.size(string)
        text = fontTreM.render(string, 1, BLACK)
        screen.blit(text, Rect(width//2-fontSize[0]//2, 100, 100,100))
        #lose money
        screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
        text=fontTreM.render(" $0",1,BLACK)
        screen.blit(text, Rect(502, 270, 100, 100)) 
        
    elif levelUp == True:
        if stageLevel<5:
            string = "YOU GOT PROMOTED!"
            fontSize = fontTreM.size(string)
            text = fontTreM.render(string, 1, BLACK)
            screen.blit(text, Rect(width//2-fontSize[0]//2, 100, 100,100))

            #earn bonus
            screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
            text=fontTreM.render("+ $300",1,BLACK)
            screen.blit(text, Rect(510, 270, 100, 100)) 

            #next level
            nextRect = draw.rect(screen,CYAN,(width//2-110,440,220,50))
            string="Next Level"
            text = fontTreS.render(string, 1, BLACK)
            fontSize = fontTreS.size(string)
            textRect = Rect(width//2-fontSize[0]//2, 450, 100,100)
            screen.blit(text, textRect)  
        else:
            string = "STAGE COMPLETED"
            text = fontTreL.render(string, 1, BLACK)
            fontSize = fontTreL.size(string)
            screen.blit(text, Rect(width//2-fontSize[0]//2, 100, 100,100))

            #earn bonus
            screen.blit(transform.scale(moneyBagPic,(77,77)),(410,250))
            text=fontTreM.render("+ $500",1,BLACK)
            screen.blit(text, Rect(510, 270, 100, 100)) 

    if button==1:
        if nextRect.collidepoint(mx,my) == True: 
            state = MAINSTATE
            if stage ==1:
                level[0] += 1
            else:
                level[1] += 1
            failList = ["2"]        #reset fail list for the next level
            money += 400            #give bonus money
        if newRect.collidepoint(mx,my) == True:     
            if gameOver == True:    
                #reset the variables for a new game
                money = 0               #lose all money
                if stage ==1:
                    level[0] = 1               #reset to level 1
                else:
                    level[1] = 1
                itemList = [0,0,0,0]    #lose all the items
                speed = 3               #reset the speed to 3
            failList = ["2"]
            state = HOMESTATE
                
    return state,level,speed,money,itemList,failList

#define/set variables
running = True
menuState = EXPLAINSTATE
myClock = time.Clock()
gameStartTime = 0
button = mx = my = 0
username = ""
locationX = 500
locationY = 700
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False 
startTimer = 0
infoMsg=""
failList=["2"]
gameOver = False
infoList=[]
level=1
lastTime = 0
lastTime2 = 0
lastTime3 = 0
lastTime4 = 0
lastTime5 = 0
numBlue = 0
circleX = []
circleY = []
circleX2 = []
circleY2 = []
circleX3 = []
circleY3=[]
portalX=[]
portalY=[]
portalX2=[]
portalY2=[]
handList = []
noteList= []
radius = 20
itemList = [0,0,0,0]
failed = False
barHeight = 0
stage=1
money = 0
gameOver = False
levelUp = False
buttonList = []
textList = []
purchaseMsg = ""
drawTime = 0
drawTime2=0
speed = 3
killPurple = False
killBlue = False
healthRecover = False
freePlay = False
clickTime = time.get_ticks()
legList = []
legTime = 0
mouthTime = 0
wingUsed = False
bombList=[]
purpleVerified=True
tooClose1=False
tooClose2=False
blueVerified=True
pillVerified = True
bombVerified = True
portalVerified= True
inputing = False
stageLevel = 1
entered = False

# Game Loop
while running:
    button = 0
    for evnt in event.get():    #checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos       #get the position of the mouse  
            button = evnt.button    #get the button type
        if evnt.type == KEYDOWN:
            if menuState==EXPLAINSTATE:
                if key.name(evnt.key) == "backspace":
                    #deletes by one if backspace key is clicked
                    username = username[:-1]                     
                elif key.name(evnt.key) == "space":
                    #add one space if space key is clicked                   
                    username+=" "    
                elif key.name(evnt.key) == "return":
                    #change to the explain state if the enter key is pressed  
                    if len(username)>=1:
                        #username has to be entered
                        entered = True
                else:
                    if len(key.name(evnt.key)) == 1:
                        #if it is more than one letter(i.e. "tabbed"), it does not show up on the screen     
                        if len(username)<14:
                            #the username should be shorter than 14 letters
                            username+=key.name(evnt.key)  #in other cases, add the key to the username 
            if menuState == GAMESTATE:
                if key.name(evnt.key) == "q":       #debugger activated
                    if itemList[2]>0:   #check if the user has the item
                        killPurple = True
                elif key.name(evnt.key) == "e":     #potion of strength activated
                    if itemList[1]>0:   #check if the user has the item
                        killBlue = True
                elif key.name(evnt.key) == "w":     #health potion activated
                    if itemList[0]>0:   #check if the user has the item
                        healthRecover = True 
            #when the key is pressed, make the corresponding key variable True
            if evnt.key == K_LEFT:
                KEY_LEFT = True
            if evnt.key == K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == K_UP:
                KEY_UP = True
            if evnt.key == K_DOWN:
                KEY_DOWN = True 
               
        if evnt.type == KEYUP:
            #when the key is released, make the corresponding key variable False
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False
                
    if KEY_LEFT == True:
        #move to left by the speed  
        locationX -= speed
        if locationX+radius<0:
            locationX = 920-radius     #go to the other side if it goes out of the screen
    if KEY_RIGHT == True:
        #move to right by the speed
        locationX += speed           
        if locationX+radius>900:
            locationX = radius       #go to the other side if it goes out of the screen
    if KEY_DOWN == True:
        #move down by the speed
        locationY += speed
        if locationY+radius>700:
            locationY = radius       #go to the top if it goes out of the screen
    if KEY_UP == True:
        #move up by the speed
        locationY -= speed     
        if locationY+radius<0:
            locationY = 700-radius     #go to the bottom if it goes out of the screen
    if menuState == EXITSTATE:
        running=False
    elif menuState == EXPLAINSTATE:
        menuState, level, money, itemList = explain(button,mx,my)
    elif menuState == HOMESTATE:
        menuState,stage,freePlay,circleX,circleY,circleX2,circleY2,numKilled,numBlue,radius,barHeight,locationX,locationY,speed = mainHome(button,mx,my,speed)
    elif menuState ==  MAINSTATE:
        menuState, gameStartTime,circleX,circleY,numKilled,circleX2,circleY2,numBlue,radius,barHeight,locationX,locationY,portalX,portalY,portalX2,portalY2,wingUsed = mainMenu(button,mx,my)
    elif menuState == GAMESTATE:
        menuState,failed,radius,locationX,locationY,killPurple,killBlue,healthRecover,itemList,numKilled,speed,wingUsed = playGame (button,locationX,locationY,radius,killPurple,killBlue,healthRecover,itemList,speed,wingUsed)
        if time.get_ticks() - legTime > 0:
            #draw the legs of the android (left side shorter)
            realLegs1 = transform.scale(leg1,(round(radius),round(radius)))
            screen.blit (realLegs1,(locationX+round(6*radius//13),locationY+round(7*radius//5)))
        if time.get_ticks() - legTime > 500:
            #draw the legs of the android (right side shorter)
            realLegs2 = transform.scale(leg2,(round(radius),round(radius)))
            screen.blit (realLegs2,(locationX+round(6*radius//13),locationY+round(7*radius//5)))
        if time.get_ticks() - legTime >= 1000:
            legTime = time.get_ticks()      #reset the time
            
        #draw the body of an android
        realAndroid = transform.scale (android,(2*round(radius),2*round(radius)))
        screen.blit (realAndroid,(locationX,locationY))    
        
        blueVerified = True
        purpleVerified = True
        pillVerified = True
        bombVerified = True
        portalVerified = True
        tooClose1 = False
        tooClose2 = False

        #blue viruses 
        if time.get_ticks() - lastTime > 700:    
            randx = randint(10, 890)         #generate a random x value
            randy = randint(10, 685)         #generate a random y value  
            if len(circleX)<1:
                circleX.append(randx)
                circleY.append(randy) 
            else:
                for y in range (0, len(circleX)):
                    distance2 = sqrt((circleX[y]-randx)**2 + (circleY[y]-randy)**2)     #no overlap with other blue viruses
                    if distance2 <= 25:
                        tooClose1=True
                        break

            if tooClose1 == False:
                for x in range (0,len(circleX2)):        #no overlap between the blue virus and the trap viruses 
                    virusesDistance1 = sqrt((circleX2[x]+15-randx)**2 + (circleY2[x]+15-randy)**2)            
                    if virusesDistance1 < 40:
                        blueVerified = False
 
                        break
            if blueVerified == True:
                circleX.append(randx)
                circleY.append(randy)     
                    
                lastTime = time.get_ticks()     #reset the lastTime variable for comparisons
                numBlue += 1            #add one to a number of blue viruses

            if len(circleX) == 6:
                #if there are more than 6 viruses on the screen, start the timer
                startTimer = time.get_ticks()  

        #purple traps   
        if time.get_ticks() - lastTime2 > 4000:
            ranNum = 0      #define the variable
            randx2 = randint(30, 860)   #generate another random x value
            randy2 = randint(30, 650)   #generate another random y value   
            
            virusDistance = sqrt((locationX-randx2)**2 + (locationY-randy2)**2) #get the distance between the user and the trap virus
            if virusDistance > 25 + radius:     #add to the list only if the trap and the user are apart
                for x in range (0,len(circleX)):        #distance btw purple traps and blue viruses
                    virusesDistance = sqrt((circleX[x]-randx2-15)**2 + (circleY[x]-randy2-15)**2) 
                    if virusesDistance < 40:
                        purpleVerified = False
                        break
                        
            if purpleVerified == True:
                if len(circleX2) < 1:
                    circleX2.append(randx2)    
                    circleY2.append(randy2)
                else:
                    for y in range (0, len(circleX2)):      #no overlap between purple viruses
                        distance1 = sqrt((circleX2[y]-randx2)**2 + (circleY2[y]-randy2)**2) 
                        if distance1 <= 35:
                            tooClose2 = True
                            break
            
            if tooClose2 == False:
                circleX2.append(randx2)     
                circleY2.append(randy2)  
            
            if len(circleX2)>15:
                randomNum = randint(1,len(circleX2))
                del circleX2[randomNum-1] 
                del circleY2[randomNum-1] 
            lastTime2 = time.get_ticks()    #reset the lastTime variable for comparisons

        #health pill 
        if radius>25:
            if time.get_ticks() - lastTime3 > 10000:    #get current time and subtract the last time
                randx3 = randint(30, 880)   #generate a random x value
                randy3 = randint(30, 670)   #generate a random y value 
                
                for x in range (0,len(circleX2)):       #no overlap with purple viruses
                    virusesDistance = sqrt((circleX2[x]+5-randx3)**2 + (circleY2[x]+5-randy3)**2)   
                    if virusesDistance < 35:
                        pillVerified = False
                        break
                if pillVerified == True:
                    circleX3.append(randx3)     #saves the x coordinates of a second circle
                    circleY3.append(randy3)     #saves the y coordinates of a second circle
                    drawTime = time.get_ticks()     #get the time where the red vaccine is drawn 
            lastTime3 = time.get_ticks()    #reset the lastTime variable for comparisons
        
        #portals
        if time.get_ticks() - lastTime4 > 10000:
            randx4 = randint(30, 820)   #generate a random x value
            randy4 = randint(30, 650)   #generate a random y value             
            randx5 = randint(30, 820)   #generate another random x value
            randy5 = randint(30, 650)   #generate another random y value  
           
            portalDistance = sqrt((randx4-randx5)**2 + (randy4-randy5)**2)      #get the distance between portals
            
            for x in range (0,len(circleX2)):
                distanceBtw1 = sqrt((circleX2[x]-randx4-15)**2 + (circleY2[x]-randy4-15)**2) 
                distanceBtw2 = sqrt((circleX2[x]-randx5-15)**2 + (circleY2[x]-randy5-15)**2) 
                if distanceBtw1 < 55 or distanceBtw2 < 55:
                    portalVerified = False
                    break 

            if portalDistance >= 300:
                if portalVerified == True:  
                    #add to the list only when the portals are certain amount apart & not close to purple traps
                    portalX.append(randx4)      
                    portalY.append(randy4)      
                    portalX2.append(randx5) 
                    portalY2.append(randy5)     

            if len(portalX)>=2:
                #if there are more than 2 portals get rid of the first one
                del portalX[0]
                del portalY[0]
                del portalX2[0]
                del portalY2[0]   
                
            lastTime4 = time.get_ticks()    #reset the lastTime variable for comparisons   
        
        #bomb
        if time.get_ticks()- lastTime5 > 9500:
            randx5 = randint(30,850)
            randy5 = randint(30,650)

            for x in range (0,len(circleX2)):       #no overlap with purple viruses
                if sqrt((circleX2[x]-randx5-15)**2 + (circleY2[x]-randy5-15)**2) < 45:
                    bombVerified = False
                    break
            if bombVerified == True:
                bombList.append(randx5)
                bombList.append(randy5)

                lastTime5 = time.get_ticks()
                drawTime2=time.get_ticks()
            
    elif menuState == RULESTATE:
        menuState = writeRule (button,mx,my)
    elif menuState == STORESTATE:
        menuState, money, purchaseMsg, infoMsg, itemList = drawStore (button,mx,my,buttonList,infoList,money,purchaseMsg,infoMsg,itemList)
    elif menuState == DONESTATE:
        menuState,stage,money,gameOver,levelUp,speed = doneGame (button,mx,my,money)
    elif menuState == INFORMSTATE:
        menuState,level,speed,money,itemList,failList = informUser(button,mx,my,level,speed,money,itemList,failList)
    elif menuState == INVSTATE:
        menuState = drawInv(button,mx,my)
    elif menuState == BOMBSTATE:
        menuState = timeBomb (button,mx,my)
      
    myClock.tick(60)    #waits long enough to have 60 fps
    display.flip()
    
quit()


#pic sources: https://www.vecteezy.com/vector-art/1340655-witch-on-a-fantasy-pop-up-book