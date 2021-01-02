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
 
CYAN = (125, 181, 172)

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
INPUTSTATE = 0
EXITSTATE = 1
EXPLAINSTATE = 2
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
bossPic = image.load("Boss.png")
bubblePic = image.load("bubble.jpeg")
angryBoss = image.load("YunaAngryBoss.jpg")
happyBoss = image.load("YunaHappyBoss.jpg")
infected = image.load("YunaInfectedImage.jpg")
congrats = image.load("YunaCongrats.jpg")
wings = image.load("YunaWing.png")
portal = image.load("YunaPortal.png")
portal = transform.scale(portal, (80,80))
portal2 = image.load("YunaPortal2.png")
portal2 = transform.scale(portal2,(80,80))
knife = image.load("YunaKnife.png")
axe= image.load("YunaAxe.png")
warningImage = image.load("warning.png")
fired = image.load("YunaFired.jpg")
promotion = image.load("YunaPromotion.jpg")
pill = image.load("YunaPill.png")
hand = image.load("YunaHand.png")
android = image.load("android.png")
leg1= image.load("legs1.jpg")
leg2= image.load("legs2.jpg")
inputing = False
helpPic = image.load("help.png")
backpackPic = image.load("backpack.png")
shopPic = image.load("shop.png")
settingPic = image.load("setting.png")
flagPic = image.load("flag.png")
computerPic = image.load("computer.png")
debugPic = image.load("debug.png")
potion1Pic = image.load("potion1.png")
potion2Pic = image.load("potion2.png")
virusPic = image.load("virus.png")
trapPic = image.load("trap.png")
moneyBagPic = image.load("moneyBag.png")
bombPic = image.load("bomb.png")

def drawArrow (x,y):
    draw.rect (screen, CYAN, (x,y,48,34))
    draw.rect (screen, WHITE, (x+10,y+10,15,14))
    draw.polygon (screen, WHITE, ((x+25,y+5),(x+25,y+29),(x+40,y+17)))

def userInput (button,mx,my):   #get the username
    state=INPUTSTATE

    level = 1
    money = 1000            #set default money as 1000
    itemList = [5,5,5,0]    #no items
    draw.rect(screen, WHITE, (0, 0, width, height))
    
    string = "CYBER BUGS"
    text = fontTreL.render(string, 1, BLACK)
    textSize = fontTreL.size(string)
    textRect = Rect(width//2-textSize[0]//2, 200, textSize[0], textSize[1])
    screen.blit(text, textRect)

    startRect = draw.rect(screen, CYAN, (width//2-140,400,280,60))
    string = "Get Started"
    text = fontTreM.render(string, 1, BLACK)
    textSize = fontTreM.size(string)
    textRect = Rect(width//2-textSize[0]//2, 407, textSize[0], textSize[1])
    screen.blit(text, textRect)

    if button == 1:
        if startRect.collidepoint(mx,my)==True:
            state = EXPLAINSTATE

    return state, level, money, itemList

def explain(button,mx,my):  #explain the scenario to the user
    global inputing

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

    if inputing == True:
        draw.rect(screen, CYAN,inputRect,2)
    if len(username)>=1:
        #user must type their username before starting a game
        if nextRect.collidepoint(mx,my) == True:
            state=HOMESTATE  
    if button == 1:
        if inputRect.collidepoint(mx,my)==True:
            inputing = True 
    return state

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
    text = fontTreXs.render("Challenge", 1, BLACK)
    screen.blit(text, Rect(292, 325, 100, 100))
    playRect = Rect(270,200,120,120)

    screen.blit(transform.scale(computerPic, (120,120)),(440,200))
    text = fontTreXs.render("Free Play", 1, BLACK)
    screen.blit(text, Rect(465, 325, 100, 100))
    freeRect =Rect(440,200,120,120)

    screen.blit(transform.scale(helpPic, (120,120)),(610,200))
    text = fontTreXs.render("Help", 1, BLACK)
    screen.blit(text, Rect(652, 325, 100, 100))
    helpRect = Rect(610,200,120,120)

    screen.blit(transform.scale(backpackPic, (120,120)),(270,400))
    text = fontTreXs.render("Inventory", 1, BLACK)
    screen.blit(text, Rect(297, 530, 100, 100))
    inventoryRect = Rect (270,400,120,120)

    screen.blit(transform.scale(shopPic, (120,120)),(440,400))
    text = fontTreXs.render("Shop", 1, BLACK)
    screen.blit(text, Rect(478, 530, 100, 100))
    storeRect = Rect(440,400,120,120)

    screen.blit(transform.scale(settingPic, (120,120)),(610,400))
    text = fontTreXs.render("Setting", 1, BLACK)
    screen.blit(text, Rect(645, 530, 100, 100))

    if button==1:
        if playRect.collidepoint(mx,my) == True:
            #if the play button is clicked, change to the main screen
            state = MAINSTATE   
            stage = randint(1,2)        #randomly choose a stage
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
            
    return state,stage, freePlay,circleX,circleY,circleX2,circleY2,numKilled,numBlue,radius,barHeight,locationX,locationY,speed

def mainMenu (button,mx,my):
    state = MAINSTATE     #define the state
    #reset variables for a new game
    gameStartTime = 0
    numKilled = 0
    circleX=[]
    circleY=[]
    circleX2=[]
    circleY2=[]    
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
    draw.rect(screen, BLACK, (0, 0, width, height))     #draw background

    #write the user's balance
    string = "$"+str(money)
    text = font2.render(string, 1, YELLOW)
    screen.blit(text, Rect(50, 50, 100, 100))      
    
    #write the rules for the specific level and stage
    if stage == 1:
        if level == 1:
            ruleText = "Get rid of 40 viruses without dying!" 
        else:
            ruleText = "Get rid of 55 viruses without dying!"
    elif stage == 2:
        if level == 1:
            ruleText = "Get rid of 30 viruses in 45 seconds!"
        else:
            ruleText = "Get rid of 40 viruses in 45 seconds!"
    elif stage == 3:
        ruleText = "Avoid the viruses!"
        
    text = font2.render(ruleText, 1, WHITE)
    screen.blit(text, Rect(250, 250, 100, 100))    
        
    #write the level and stage
    string = "Level: " + str(level) +"     Stage: " + str(stage)
    text = font2.render(string, 1, WHITE)
    screen.blit(text, Rect(350, 50, 100, 100))
    
    #draw&write the start option
    startRect = Rect(350, 360, 300, 60) 
    draw.rect(screen, PINK, startRect)
    string = "START"
    text = font3.render(string, 1, WHITE)
    screen.blit(text, Rect(440, 370, 100, 100))
    
    #draw&write the back option
    backRect = Rect(900, 0, 100, 50) 
    draw.rect(screen, GREY, backRect)    
    string = "BACK"
    text = font1.render(string, 1, WHITE)
    screen.blit(text, Rect(920, 10, 100,100))      
        
    if button==1:
        if startRect.collidepoint(mx,my)==True:
            state = GAMESTATE       #change to the game screen when the button is clicked
            #reset variables for the next game
            circleX=[]
            circleY=[]
            circleX2=[]
            circleY2=[]            
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
            #go back if the back button is clicked
            state = HOMESTATE
        
    return state,gameStartTime,circleX,circleY,numKilled,circleX2,circleY2,numBlue,radius,barHeight,locationX,locationY,portalX,portalY,portalX2,portalY2,wingUsed

def writeRule (button,mx,my):
    #inform the user about the rules
    state = RULESTATE
    draw.rect(screen, WHITE, (0, 0, width, height))      
    
    #show the picture that has rules in
    rulePic = image.load ("YunaRules.png")
    screen.blit(rulePic,(100,50))
    
    #back button
    drawBack()
    backRect = Rect(width-75,0,80,37)
        
    if backRect.collidepoint(mx,my) == True:
        state=HOMESTATE  
        
    return state

def playGame (button,locationX,locationY,radius,killPurple,killBlue,healthRecover,itemList,speed,wingUsed):
    #free play state
    global barHeight, startTimer
    state = GAMESTATE  

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
        itemList[3] -= 0.2  
    elif level == 1:        #if the level is one and the user does not have a wing item
        speed = 3           #speed is 3
    elif level == 2:        #if the level is two and the user does not have a wing item
        speed = 4           #speed is 4
    if wingUsed == True:
        #increase the speed if the wing is used
        speed += 0.7
        realWings = transform.scale (wings,(3*round(radius),3*round(radius)//2))  #draw wings to the android
        screen.blit(realWings,(locationX-round(radius)//2,locationY))

    if freePlay == True: 
        #free play mode
        if radius>20:       
            for a in range (0,len(circleX3)):    
                #draw the pill only when radius is higher than 30
                screen.blit(transform.scale(pill,(30,30)),(circleX3[0],circleY3[0]))     
                
                #calculate the distance between the center of the circle and the pill image
                distance = sqrt((circleX3[0]+14-locationX-radius)**2+(circleY3[0]+14-locationY-radius)**2)
                
                if distance < radius+18:  #sum of the radius and the pill image
                    radius -= 7     #decrease the radius by 7
                    #get rid of the collided pill image's coordinates from the list
                    del circleX3[0]
                    del circleY3[0]                    

                if time.get_ticks()-drawTime>3500:
                    #get rid of the pill image's coordinate from the list after three seconds it is created
                    del circleX3[0]
                    del circleY3[0]  
        for i in range (0,len(bombList)//2):
            screen.blit(transform.scale(bombPic,(70,70)),(bombList[0],bombList[1]))
            bombDistance = sqrt((bombList[0]+17-locationX-radius)**2+(bombList[1]+17-locationY-radius)**2)
            if bombDistance <radius+20:
                state=DONESTATE
                bombList.clear()
            if time.get_ticks()-drawTime2 > 7000:
                bombList.clear()
        
        if time.get_ticks()-startTimer>=2000:       #health bar decreases at a dif rate depending on the #viruses
            if 13>len(circleX)>=8:
                barHeight+=0.15
            elif 20>len(circleX)>=13:
                barHeight+=0.2
            elif 25>len(circleX)>=20:
                barHeight+=0.25
            elif len(circleX)>=25:
                barHeight+=0.3

        if barHeight>=344:
            state = DONESTATE   #the game finishes when the health is zero
            
        for b in range (0,len(circleX2)):   #purple traps
            screen.blit(transform.scale(trapPic,(59,59)), (circleX2[b],circleY2[b]))   #draw purple trap viruses
            #calculate the distance between the center of the circles
            distance = sqrt((circleX2[b]+29-locationX-radius)**2+(circleY2[b]+29-locationY-radius)**2)
            if distance < radius+20:    #sum of the radii's 
                purpleHit = True

        if purpleHit == True:
            barHeight+=0.6          #decreases health
            speed -= 0.3 
            purpleHit = False   
        x=0    
        while x<len(circleX):       #blue viruses
            screen.blit(transform.scale(virusPic,(32,32)), (circleX[x],circleY[x]))

            #calculate the distance between the center of the circles
            distance = sqrt((circleX[x]+15-locationX-radius)**2+(circleY[x]+15-locationY-radius)**2)
    
            if distance < radius+15:  #sum of the radii's            
                #get rid of the collided virus's coordinates from lists
                del circleX[x]  
                del circleY[x]
                radius+=0.7   #makes the size of the android larger
            x+=1
        
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
            killBlue = False        #set the variable to false again
            
            if len(circleX) >= 3:
                #check if there is more than three blue viruses
                for i in range (0,3):   #get rid of a random blue virus
                    anotherNum = randint(0,len(circleX)-1)  
                    del circleX[anotherNum]
                    del circleY[anotherNum]
            else:
               for i in range (0,len(circleX)):   #get rid of a random blue virus
                    anotherNum = randint(0,len(circleX)-1)  
                    del circleX[anotherNum]
                    del circleY[anotherNum] 
                
        if healthRecover == True:
            itemList[0] -= 1        #subtract one from the list
            healthRecover = False   #set the variable to false again      
            if barHeight > 0:       #check if the bar has started decreasing
                barHeight -= 25     #make the height of the health bar become higher by 20
                 
    else:
        x = 0 
        while x < len(portalX): 
            screen.blit(portal,(portalX[x],portalY[x]))     #draw an enter portal
            screen.blit(portal2,(portalX2[x],portalY2[x]))  #draw an exit portal
            portalRect = Rect (portalX[x],portalY[x],80,80) #define the portal rect
            
            if portalRect.collidepoint(locationX+radius,locationY+radius) == True:
                #change the location to the exit portal
                locationX = portalX2[x]  + radius
                locationY = portalY2[x]  
                
                #get rid of the portals from the list
                del portalX[x]      #enter portal
                del portalY[x]            
                del portalX2[x]     #exit portal
                del portalY2[x]
            x+=1          

        if radius>30:    
            for a in range (0,len(circleX3)):  
                #draw the red vaccine only when radius is higher than 30
                screen.blit(transform.scale(pill,(30,30)),(circleX3[0],circleY3[0]))    
                
                #calculate the distance between the center of the circle and the pill image
                distance = sqrt((circleX3[0]-locationX-radius)**2+(circleY3[0]-locationY-radius)**2)
                
                if distance < radius+10:  #sum of the radius and the pill image
                    radius -= 7     #decrease the radius by 7 
                    #get rid of the collided pill image's coordinates from the list
                    del circleX3[0]
                    del circleY3[0]                    

                if time.get_ticks()-drawTime>3000:
                    #get rid of the pill image's coordinate from the list after three seconds it is created
                    del circleX3[0]
                    del circleY3[0]    
        
        if time.get_ticks()-startTimer>=3000 and len(circleX)>=10:
            #increase the health decrease bar when there are more than 10 viruses alive and stayed that way for 3 or more seconds
            barHeight+=0.2
            
        if barHeight>=344:
            state = DONESTATE   #the game finishes when the health is zero
            failed = True       #"failed" becomes true
            
        for b in range (0,len(circleX2)):
            draw.circle(screen, PURPLE, (circleX2[b],circleY2[b]),15)   #draw  purple trap viruses
    
            #calculate the distance between the center of the circles
            distance = sqrt((circleX2[b]-locationX-radius)**2+(circleY2[b]-locationY-radius)**2)
            
            if distance < radius+15:    #sum of the radii's 
                state = DONESTATE       #the game finishes when collide with purple viruses
                failed = True           #"failed" becomes true
                print("you collided with a trap virus.")
                
        if killPurple == True:
            #check if 'w' key is pressed
            itemList[2] -= 1        #subtract one from the list 
            killPurple = False      #set the variable to false again 
            
            if len(circleX2) > 0:
                #check if there is more than one purple virus
                ranNum = randint(0,len(circleX2)-1) #get a random number
                #get rid of a random purple virus
                del circleX2[ranNum]
                del circleY2[ranNum]

        if killBlue == True:
            #check if 'e' key is pressed
            itemList[1] -= 1        #subtract one from the list 
            killBlue = False        #set the variable to false again
            
            if len(circleX) > 0:
                #check if there is more than one blue virus
                anotherNum = randint(0,len(circleX)-1)  #get a random number
                #get rid of a random blue virus
                del circleX[anotherNum]
                del circleY[anotherNum]
                
        if healthRecover == True:
            #check if 'r' key is pressed
            itemList[0] -= 1        #subtract one from the list 
            healthRecover = False   #set the variable to false again           
            if barHeight > 0:       #check if the bar has started decreasing
                barHeight -= 20     #make the height of the health bar become higher by 20
                
        x=0    
        while x<len(circleX):
            #draw normal blue viruses
            screen.blit(transform.scale(virusPic,(10,10)), (circleX[x],circleY[x]))
            
            #calculate the distance between the center of the circles
            distance = sqrt((circleX[x]-locationX-radius)**2+(circleY[x]-locationY-radius)**2)
    
            if distance < radius+7:  #sum of the radii's            
                #get rid of the collided circle's coordinates from lists
                del circleX[x]  
                del circleY[x]
                radius+=1   #makes the size of the android larger
            x+=1
            
        if stage == 1:
            if level == 1:
                if numKilled >= 40:
                    #stage one, level one ends when 40 viruses are killed
                    state = DONESTATE
            elif level == 2:
                if numKilled >= 55:
                    #stage one, level two ends when 55 viruses are killed
                    state = DONESTATE
                    
        if stage == 2:
            #write the time
            #add zeros so that all the time has the same length (e.g. 348 milliseconds and 1930 into 00348 and 01930)
            if len(str(time.get_ticks() - gameStartTime))<4:
                a = "00" + str(time.get_ticks() - gameStartTime)
            elif len(str(time.get_ticks() - gameStartTime))<5:
                a = "0"+str(time.get_ticks() - gameStartTime)
            else:
                a = str(time.get_ticks() - gameStartTime)
                
            string = a[:2] +":"+ a[2:4]     #make it into a time format (e.g. 1230 into 12:30) 
            text = font1.render(string, 1, WHITE)
            screen.blit(text, Rect(933, 600, 100, 100)) 
            
            if 40000<time.get_ticks()-gameStartTime<40200 or 40500<time.get_ticks()-gameStartTime<40700:
                screen.blit(transform.scale(warning,(100,100)),(10,10))  #draw a warning sign at 40 second
                
            if time.get_ticks()-gameStartTime>45000:
                if level == 1:
                    if numKilled>=30:
                        #stage two, level one ends when more than 30 viruses are killed in 45 seconds
                        state = DONESTATE
                    else:
                        state = DONESTATE           
                        failed=True         #fail when not enough viruses were killed.                    
                elif level == 2:
                    if numKilled>=40:
                        #stage two, level two ends when more than 40 viruses are killed in 45 seconds
                        state = DONESTATE
                    else:
                        state = DONESTATE           
                        failed=True         #fail when not enough viruses were killed.
            
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
    global failList, circleX, circleY,circleX2,circleY2,numKilled, numBlue, radius, barHeight, locationX, locationY, speed
    state = DONESTATE  
    stage = 1
    gameOver = False
    levelUp = False    
    draw.rect(screen, GREY, (0, 0, width, height))
    
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
        if failed == True:      #when the user fails
            screen.blit(transform.scale(angryBoss, (300,300)), Rect(70,300,200,200))       #display an angry boss image
            screen.blit(transform.scale(infected, (400,200)), (370,250))        #display an infected sign            
        elif failed == False:   #when the user succeeds
            screen.blit(happyBoss, Rect(50,300,200,200))       #display a happy boss image
            for x in range (10,170):
                screen.blit(transform.scale(congrats, (750,200)), (300,x))        #display a congratulation sign 
            
    if button == 1:
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
                stage = randint(1,2)    #randomly chooses a stage for the next game
                if failed == True:
                    if failList[-1] != "0":                
                        failList=[]             #clear the list if the previous one is not zero
                    failList.append ("0")       #if failed, add zero
                    if len(failList) == 3: 
                        #Game-over if there are three consecutive fails
                        gameOver = True
                        state = INFORMSTATE #go to the inform screen to show game-osver
                    else:
                        state = MAINSTATE   #go back to the main screen
                elif failed == False:
                    money+=100      #get paid when succeed                   
                    if failList[-1] != "1":            
                        failList=[]             #clear the list if the previous one is not one
                    failList.append ("1")       #if succeeded, add one 
                    if len(failList) == 3:
                        #level up if there are three consecutive success
                        levelUp = True
                        state = INFORMSTATE #go to the inform screen to show level up
                    else:
                        state = MAINSTATE   #go back to the main screen

    return state,stage,money,gameOver,levelUp

def informUser (button,mx,my,level,speed,money,itemList,failList):
    #inform the user about game over or level up
    state = INFORMSTATE     #define the state
    draw.rect (screen,WHITE,(0,0,width,height))     #draw the background
    
    #draw&write a button to go back to the main screen
    newRect = Rect(360,575,300,50)
    draw.rect(screen,PINK,newRect)
    string="BACK TO MAIN SCREEN"
    text = font1.render(string, 1, WHITE)
    textRect = Rect(370, 590, 100,100)
    screen.blit(text, textRect)  

    if gameOver == True:
        #if it is game over, draw a note that is decreasing in size
        if len(noteList) <5:
            for x in range (10,5,-1):
                #add the picture to the list in different sizes
                note = transform.scale(fired,(x*30,x*30))       
                noteList.append(note)
            for x in range(0,5):
                #show the picture with a 70 millisecond of delay
                draw.rect(screen,WHITE,(0,0,width,570))
                screen.blit(noteList[x],(300,180))
                display.flip()
                time.delay(70)
        else:
            screen.blit(transform.scale(fired,(150,150)),(300,180)) #after the loop ends it stays. 
        
    elif levelUp == True:
        if level == 2:
            #notice that the user has finished the game
            string = "GOOD BYE! TIME TO RETIRE..."
            text = font1.render(string, 1, BLACK)
            screen.blit(text, Rect(300, 470, 100,100))
        else:
            screen.blit (transform.scale(promotion,(450,200)), (250,200))   #notice that the user is promoted (level up)
            string = "YOU GOT PROMOTED!"
            text = font1.render(string, 1, BLACK)
            screen.blit(text, Rect(370, 470, 100,100))
    
    if button==1:
        if newRect.collidepoint(mx,my) == True:     
            if gameOver == True or (levelUp == True and level == 2):    
                #go to the home state if the user is fired or the user finished the entire game
                state = HOMESTATE
                #reset the variables for a new game
                money = 0   #lose all money
                level = 1           #reset to level 1
                itemList = [0,0,0,0]  #lose all the items
                failList = ["2"]    #reset fail list for the new game
                speed = 3   #reset the speed to 3
            elif levelUp == True:
                #go back to the home screen when the button is clicked
                state = MAINSTATE
                level+=1            #add one to level
                failList = ["2"]    #reset fail list for the next level
                speed = 4           #speed gets faster
                money += 400        #give bonus money
                
    return state,level,speed,money,itemList,failList

#define/set variables
running = True
menuState = INPUTSTATE
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
verified=True
tooClose1=False
tooClose2=False

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
                        state = MAINSTATE          
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
            locationX = 900     #go to the other side if it goes out of the screen
    if KEY_RIGHT == True:
        #move to right by the speed
        locationX += speed           
        if locationX+radius>900:
            locationX = 0       #go to the other side if it goes out of the screen
    if KEY_DOWN == True:
        #move down by the speed
        locationY += speed
        if locationY+radius>700:
            locationY = 0       #go to the top if it goes out of the screen
    if KEY_UP == True:
        #move up by the speed
        locationY -= speed     
        if locationY+radius<0:
            locationY = 700     #go to the bottom if it goes out of the screen
    if menuState == INPUTSTATE: 
        menuState, level, money, itemList = userInput(button, mx, my)
    elif menuState == EXITSTATE:
        running=False
    elif menuState == EXPLAINSTATE:
        menuState = explain(button,mx,my)
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
 
        if time.get_ticks() - lastTime > 1000:    #blue viruses 
            randx = randint(10, 890)         #generate a random x value
            randy = randint(10, 685)         #generate a random y value  
            if len(circleX)<1:
                circleX.append(randx)
                circleY.append(randy) 
            else:
                for y in range (0, len(circleX)):
                    distance2 = sqrt((circleX[y]-randx)**2 + (circleY[y]-randy)**2)
                    if distance2 <= 15:
                        tooClose1=True
                        break
            if tooClose1 == False:
                circleX.append(randx)
                circleY.append(randy)     
                    
                lastTime = time.get_ticks()     #reset the lastTime variable for comparisons
                numBlue += 1            #add one to a number of blue viruses
            
            if len(circleX) == 10:
                #if there are more than 10 viruses on the screen, start the timer
                startTimer = time.get_ticks()  
                
        if time.get_ticks() - lastTime2 > 4000:    #purple trap
            ranNum = 0      #define the variable
            randx2 = randint(30, 880)   #generate another random x value
            randy2 = randint(30, 670)   #generate another random y value   
            
            virusDistance = sqrt((locationX-randx2)**2 + (locationY-randy2)**2) #get the distance between the user and the trap virus
            if virusDistance > 25 + radius:     #add to the list only if the trap and the user are apart
                for x in range (0,len(circleX)):
                    virusesDistance = sqrt((circleX[x]-randx2)**2 + (circleY[x]-randy2)**2) #get the distance between the blue viruses and the trap virus            
                    if virusesDistance < 30:
                        #make it impossible to overlap any of the blue virus
                        verified = False
                        break
                        
            if verified == True:
                if len(circleX2) < 1:
                    circleX2.append(randx2)    
                    circleY2.append(randy2)
                else:
                    for y in range (0, len(circleX2)):
                        distance1 = sqrt((circleX2[y]-randx2)**2 + (circleY2[y]-randy2)**2)
                        if distance1 <= 20:
                            tooClose2 = True
                            break
            if tooClose2 == False:
                circleX2.append(randx2)     
                circleY2.append(randy2)   
            lastTime2 = time.get_ticks()    #reset the lastTime variable for comparisons
                
        if time.get_ticks()-gameStartTime>20000:
            if time.get_ticks() - lastTime3 > 10000:    #get current time and subtract the last time
                #circleX3=[]
                #circleY3=[]
                
                randx3 = randint(30, 900)   #generate a random x value
                randy3 = randint(30, 670)   #generate a random y value 
                
                circleX3.append(randx3)     #make a list that saves the x coordinates of a second circle
                circleY3.append(randy3)     #make a list that saves the y coordinates of a second circle
                
                lastTime3 = time.get_ticks()    #reset the lastTime variable for comparisons
                drawTime = time.get_ticks()     #get the time where the red vaccine is drawn 
        if time.get_ticks()- lastTime5 > 10000:
            randx5 = randint(30,800)
            randy5 = randint(30,700)

            bombList.append(randx5)
            bombList.append(randy5)

            lastTime5 = time.get_ticks()
            drawTime2=time.get_ticks()
        if time.get_ticks() - lastTime4 > 10000:
            randx4 = randint(30, 800)   #generate a random x value
            randy4 = randint(30, 700)   #generate a random y value             
            randx5 = randint(30, 800)   #generate another random x value
            randy5 = randint(30, 700)   #generate another random y value  
           
            portalDistance = sqrt((randx4-randx5)**2 + (randy4-randy5)**2)      #get the distance between portals
            
            if portalDistance >= 300:    
                #add to the list only when the portals are certain amount apart
                portalX.append(randx4)      #make a list that saves the x coordinates of a enter portal
                portalY.append(randy4)      #make a list that saves the y coordinates of a enter portal
                portalX2.append(randx5)     #make a list that saves the x coordinates of a exit portal
                portalY2.append(randy5)     #make a list that saves the y coordinates of a exit portal

            if len(portalX)>=3:
                #if there are more than 2 portals get rid of the first one
                del portalX[0]
                del portalY[0]
                del portalX2[0]
                del portalY2[0]   
                
            lastTime4 = time.get_ticks()    #reset the lastTime variable for comparisons   
            
    elif menuState == RULESTATE:
        menuState = writeRule (button,mx,my)
    elif menuState == STORESTATE:
        menuState, money, purchaseMsg, infoMsg, itemList = drawStore (button,mx,my,buttonList,infoList,money,purchaseMsg,infoMsg,itemList)
    elif menuState == DONESTATE:
        menuState,stage,money,gameOver,levelUp = doneGame (button,mx,my,money)
    elif menuState == INFORMSTATE:
        menuState,level,speed,money,itemList,failList = informUser(button,mx,my,level,speed,money,itemList,failList)
    elif menuState == INVSTATE:
        menuState = drawInv(button,mx,my)
      
    myClock.tick(60)    #waits long enough to have 60 fps
    display.flip()
    
quit()


#pic sources: https://www.vecteezy.com/vector-art/1340655-witch-on-a-fantasy-pop-up-book