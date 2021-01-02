from pygame import *     
from random import *   
import os

from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT
from pygame.draw import circle 

init()   
size = width, height = 800, 600
screen = display.set_mode(size)     #sets the screen

#winSound = mixer.Sound("Mario.ogg") 
   	 	
#set the colours
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)        
WHITE = (255,255,255)

OLDROSE = (193, 129, 129)
DARKPINK = (180, 68, 107)
LIGHTPINK = (255, 222, 217)

GRAY = (217, 208, 206)
PINK = (238, 214, 202)


#set fonts
fontRavie = font.SysFont("ravie", 70)
fontComic = font.SysFont("comicsansms", 25)
fontCon = font.SysFont ("consolas", 40)
fontConM = font.SysFont ("consolas", 32)
fontConL = font.SysFont ("consolas", 37)
fontConS = font.SysFont ("consolas", 27)
fontConXs = font.SysFont ("consolas", 21)

#define the states
MAINSTATE = 0
LOGINSTATE = 1
REGISTERSTATE = 2
HOMESTATE = 4
CHOOSESTATE=5
SOLITAIRE = 6
SCORESTATE=7
TWOPLAYER=8
LEADERBOARD=9
MULTISCORESTATE=10
SECONDHOME=11
HELPSTATE =12
SETTINGSTATE = 13
DELSTATE = 14

#images
helpPic = image.load("C:/Users/yuna0/Desktop/Coding/Rack-O/helpIcon.png")
settingPic = image.load("C:/Users/yuna0/Desktop/Coding/Rack-O/settingsIconSolid.png")
startPic = image.load("C:/Users/yuna0/Desktop/Coding/Rack-O/startIcon.png")
rulePic = image.load("C:/Users/yuna0/Desktop/Coding/Rack-O/rule.png")

def mainMenu (button, mouseX, mouseY):
    global screen, width, height
    state = MAINSTATE     
    draw.rect(screen, PINK, (0, 0, width, height))
    
    #RACK-O logo at the top
    string = "RACK-O" 
    text = fontRavie.render(string, 1, BLACK)
    textSize = fontRavie.size(string)
    textRect = Rect(width//4 + (width//2 - textSize[0])//2, 100, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #login box
    loginRect = Rect(170, 240, round(0.27*width), height//10) 
    draw.rect(screen, WHITE, loginRect)
    string = "LOG IN"
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(210, 253, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #register button
    registerRect = Rect(414, 240, round(0.27*width), height//10) 
    draw.rect(screen, WHITE, registerRect)
    string = "REGISTER"
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(434, 253, textSize[0], textSize[1])
    screen.blit(text, textRect)

    if button==1:
        if loginRect.collidepoint(mouseX,mouseY)==True:       
            state = LOGINSTATE
        elif registerRect.collidepoint(mouseX, mouseY)==True:       
            state = REGISTERSTATE  
         
    return state

def drawBoxes():
    draw.rect(screen,PINK,(0,0,width,height))  
    #draw the boxes for writing the username and password
    box1 = Rect(175,200,450,40)
    box2 = Rect(175,300,450,40)  
    draw.rect(screen,WHITE,box1)    
    draw.rect(screen,WHITE,box2)  

    #write USER ID    
    string="USER ID:"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(175, 164, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    #write PASSWORD     
    string="PASSWORD:"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(175, 264, textSize[0], textSize[1])
    screen.blit(text, textRect) 
    
def drawExit():
    #exit button
    exitRect = Rect(755, 15, 30, 30)
    draw.rect(screen, DARKPINK, exitRect)
    string = "X"
    text = fontComic.render(string, 1, WHITE)
    textSize = fontComic.size(string)
    textRect = Rect(761, 12, textSize[0], textSize[1])
    screen.blit(text, textRect) 

def drawRegister(button, mouseX, mouseY):
    global username, password, registered
    state=REGISTERSTATE
    find=False
    entered=False
    error1=False
    usernameIn=False
    pwIn=False
    multiple=False
    drawBoxes() 
    drawExit()  
    nameList=[]
    pwList=[]    
    scoreList=[]
    box1 = Rect(175,200,450,50)
    box2 = Rect(175,300,450,50) 
    startRect=Rect(width//2-110,260,220,50)

    string = "REGISTER"
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2-textSize[0]//2, 60, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    #write NEXT  
    endRect = Rect(525,420,100,40) 
    draw.rect(screen, WHITE, endRect)   
    string = "NEXT"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(545, 426, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    #link to LOG IN  
    insteadRect = Rect(175,434,180,30) 
    draw.line (screen, BLACK, (175,453),(353, 453), 2) 
    string = "Sign in instead"
    text = fontConXs.render(string, 1, BLACK)
    textSize = fontConXs.size(string)
    textRect = Rect(175, 434, textSize[0], textSize[1])
    screen.blit(text, textRect)   
    
    exitRect = Rect(755, 15, 30, 30)    #exit button
    
    if box1.collidepoint(mouseX,mouseY):
        string = "USER ID:"        
        usernameIn = True
        pwIn = False
        text = fontConS.render(string, 1, OLDROSE)
        textSize = fontConS.size(string)
        textRect = Rect(175, 164, textSize[0], textSize[1])
        screen.blit(text, textRect) 

    if box2.collidepoint(mouseX,mouseY):
        string = "PASSWORD:"
        text = fontConS.render(string, 1, OLDROSE)
        textSize = fontConS.size(string)
        textRect = Rect(175, 264, textSize[0], textSize[1])
        screen.blit(text, textRect)          
        usernameIn = False
        pwIn = True

    string = password
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(181,308,450,50) 
    screen.blit(text, textRect) 

    string = username
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(181,208,450,50)
    screen.blit(text, textRect)  
  
    if endRect.collidepoint(mouseX,mouseY):
        entered = True

    if entered:
        error1 = False       
        try:
            numFile = open ("thing.dat", "r")
            find = True
        except:
            print("No database.")
        if find==True:
            while True:
                text = numFile.readline()
                #rstrip removes the newline character read at the end of the line
                text = text.rstrip("\n")     
                if text=="": 
                    break
                data=text.split("*")
                nameList.append(data[0])
                pwList.append(data[1])
                scoreList.append(data[2])
            numFile.close()
            if nameList.count(username)>0:      #checks if the username already exists
                multiple=True             
        if multiple==False:
            numFile = open("thing.dat", "w")
            for i in range(0, len(nameList)):
                numFile.write(nameList[i]+"*"+ pwList[i]+"*"+scoreList[i]+"\n")  
            numFile.write(username+"*"+password+"*"+"0"+"\n") 
            numFile.close() 
            registered=True  
        if multiple==True:
            error1=True 
        multiple=False
        entered = False
        password=""   
        username=""
    if error1 == True:
        #username already taken                       
        string = "This username already exists."
        text = fontConXs.render(string, 1, BLACK)
        textSize = fontConXs.size(string)
        textRect = Rect(181, 212, textSize[0], textSize[1])
        screen.blit(text, textRect)   

    if registered==True:
        draw.rect(screen,PINK,(0,0,width,height))
        string = "You are now registered."
        text = fontCon.render(string, 1, BLACK)
        textSize = fontCon.size(string)
        textRect = Rect(width//2-textSize[0]//2,200-textSize[1]//2,textSize[0],textSize[1])
        screen.blit(text, textRect) 

        draw.rect(screen,WHITE,startRect)
        string = "Get Started"
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(317,274,textSize[0],textSize[1])
        screen.blit(text, textRect) 

    if button == 1:
        if insteadRect.collidepoint(mouseX,mouseY)==True:
            state = LOGINSTATE
            registered=False
        elif exitRect.collidepoint(mouseX,mouseY)==True:
            state = MAINSTATE
            registered=False
        if registered == True:
            if startRect.collidepoint(mouseX,mouseY)==True:
                state = LOGINSTATE
                registered=False
    if button == 3:
        state = MAINSTATE 

    return state,entered,pwIn,usernameIn

def drawLogin(button,mouseX,mouseY,nameList,pwList,scoreList):
    global username,password,find, secondLogin
    state=LOGINSTATE    
    exist=False
    error2=False   
    usernameIn=False
    pwIn=False
    entered=False
    username2=""    
    password2=""
    nameList=[]
    pwList=[]  
    scoreList=[]    
    drawBoxes()
    drawExit()   

    string = "LOG IN"
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2-textSize[0]//2, 60, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    #log in button
    doneRect=Rect(width//2-75,403,150,45)
    draw.rect(screen,WHITE,doneRect)
    string = "LOG IN"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2-75+27,415, textSize[0], textSize[1])
    screen.blit(text, textRect)  
      
    box1 = Rect(175,200,450,50)
    box2 = Rect(175,300,450,50)   

    exitRect = Rect(755, 15, 30, 30)    #exit button

    if secondLogin==True:
        string="Please log in for the second user."
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(width//2-textSize[0]//2, 115, textSize[0], textSize[1])
        screen.blit(text, textRect)   

    if box1.collidepoint(mouseX,mouseY)==True:
        usernameIn=True
        pwIn=False
        string="USER ID:"
        text = fontConS.render(string, 1, OLDROSE)
        textSize = fontConS.size(string)
        textRect = Rect(175, 164, textSize[0], textSize[1])
        screen.blit(text, textRect) 

    elif box2.collidepoint(mouseX,mouseY)==True:
        usernameIn=False
        pwIn=True
        string="PASSWORD:"
        text = fontConS.render(string, 1, OLDROSE)
        textSize = fontConS.size(string)
        textRect = Rect(175, 264, textSize[0], textSize[1])
        screen.blit(text, textRect)  

    string=username
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(181,208,450,50)
    screen.blit(text, textRect) 

    string=password
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(181,308,450,50)
    screen.blit(text, textRect) 

    if doneRect.collidepoint(mouseX,mouseY)==True:
        entered=True         

    if entered==True:            
        try:
            numFile = open ("thing.dat", "r")
            find=True
        except:
            print("No database.")
        if find==True:
            while True:
                text = numFile.readline()
                #rstrip removes the newline character read at the end of the line
                text = text.rstrip("\n")     
                if text=="" or text=="*": 
                    break
                data=text.split("*") 
                nameList.append(data[0])
                pwList.append(data[1]) 
                scoreList.append(data[2])                  
            numFile.close()
            for i in range (0,len(nameList)):
                if str(nameList[i])==str(username) and str(pwList[i])==str(password):
                    exist=True
                    error2=False  
                    break
                else:                
                    error2=True
            if exist==True:
                if secondLogin==True:
                    state=SECONDHOME
                    username2=username
                    password2=password
                else:
                    state=HOMESTATE
        entered=False
    if error2 == True:
        #wrong pw                      
        string = "Not registered / Wrong password"
        text = fontConXs.render(string, 1, BLACK)
        textSize = fontConXs.size(string)
        textRect = Rect(width//2 - textSize[0]//2, 362, textSize[0], textSize[1])
        screen.blit(text, textRect)        
    if button==3:
        state = MAINSTATE
    if button==1:
        if exitRect.collidepoint(mouseX,mouseY) == True:
            if secondLogin == False:
                state = MAINSTATE
            else:
                state = HOMESTATE
                secondLogin = False
                username = username1
    return state,entered,pwIn,usernameIn,username2,password2,nameList,pwList,scoreList,username1,password1

def drawHome(button, mouseX, mouseY): 
    global username, password, secondLogin          
    state = HOMESTATE 
    drawExit()
    draw.rect(screen, PINK, (0, 0, width, height)) 
    if secondLogin == False:
        string = "WELCOME, %s" %username 
    else:
        string = "WELCOME, " + str(username1) + ", " + str(username2)
      
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 60, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #help button
    helpCircle = draw.circle (screen, PINK, (235,267), 42)
    smallHelpPic = transform.scale(helpPic, (60,60))
    screen.blit(smallHelpPic, (206,240))

    #start button
    startCircle = draw.circle(screen, WHITE,(400, 267), 60)
    smallStartPic = transform.scale(startPic, (130, 130))
    screen.blit(smallStartPic, (width//2-66, 204)) 
       
    #settings button
    settingCircle = draw.circle (screen, PINK, (565,267), 42)
    smallSettingPic = transform.scale(settingPic, (60,60))
    screen.blit(smallSettingPic, (535,238))  

    #log out button
    logOutRect = Rect(width//2-63, 490, 126, 35)     
    draw.line (screen, BLACK, (width//2-63, 524),(width//2+63,524),2)
    string = "Log Out"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 495, textSize[0], textSize[1])
    screen.blit(text, textRect)     

    #scoreboard button
    leaderRect = Rect(width//3, 405, width//3, height//12) 
    draw.rect(screen, OLDROSE, leaderRect)
    string = "LEADERBOARD"
    text = fontConM.render(string, 1, WHITE)
    textSize = fontConM.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 415, textSize[0], textSize[1])
    screen.blit(text, textRect)  

    if button == 1:
        if startCircle.collidepoint(mouseX,mouseY) == True:        
            state = CHOOSESTATE
        elif helpCircle.collidepoint(mouseX,mouseY) == True:    
            state = HELPSTATE
        elif settingCircle.collidepoint(mouseX,mouseY) == True:    
            state = SETTINGSTATE
        elif leaderRect.collidepoint(mouseX, mouseY) == True: 
            state = LEADERBOARD  
        elif logOutRect.collidepoint(mouseX, mouseY) == True: 
            state = MAINSTATE
            username=""
            password=""
            secondLogin = False

    return state

def help (button, mouseX, mouseY):
    state = HELPSTATE

    screen.blit(rulePic, (0,0))
    drawExit()
    exitRect = Rect(755, 15, 30, 30) 

    if button == 1:
        if exitRect.collidepoint(mouseX, mouseY) == True:
            state = HOMESTATE
    elif button == 3:
        state = HOMESTATE
    return state

def setting (button, mouseX, mouseY):
    global themeColor, maxScore
    state = SETTINGSTATE
    draw.rect(screen, PINK, (0, 0, width, height))
    drawExit()
    exitRect = Rect(755, 15, 30, 30)

    #write "SETTINGS" at the top
    string = "SETTINGS" 
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2-textSize[0]//2, 40, textSize[0], textSize[1])
    screen.blit(text, textRect)

    string = "Colour Theme" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(60, 168, textSize[0], textSize[1])
    screen.blit(text, textRect)

    redRect = draw.rect (screen, RED, (310, 155, 50, 50))
    greenRect = draw.rect (screen, GREEN, (380, 155, 50, 50))
    blueRect = draw.rect (screen, BLUE, (450, 155, 50, 50))
    outline (redRect,2)
    outline (greenRect,2)
    outline (blueRect,2)

    string = "Max Score to Win (multiplayers only)" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(60, 240, textSize[0], textSize[1])
    screen.blit(text, textRect)

    for i in range (1,6):
        draw.rect(screen, WHITE, (60+90*(i-1), 285, 80, 34))
        string=str(50*i)
        textSize = fontConXs.size(string)
        text = fontConXs.render(string, 1, BLACK)
        screen.blit(text, Rect(82+90*(i-1), 293, textSize[0], textSize[1]))
    
    rect1 = Rect(60, 285, 80, 34)
    rect2 = Rect(150, 285, 80, 34)
    rect3 = Rect(240, 285, 80, 34)
    rect4 = Rect(330, 285, 80, 34)
    rect5 = Rect(420, 285, 80, 34)

    saveRect = draw.rect (screen, WHITE, (270,390,260,50))
    draw.rect (screen, OLDROSE, saveRect, 3)
    string = "Save Changes" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2-textSize[0]//2, 402, textSize[0], textSize[1])
    screen.blit(text, textRect)

    delRect = draw.rect (screen, WHITE, (270,460,260,50))
    draw.rect (screen, OLDROSE, delRect, 3)
    string = "Delete Account" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2-textSize[0]//2, 472, textSize[0], textSize[1])
    screen.blit(text, textRect)

    if maxScore == 50:
        outline(rect1, 3)
    elif maxScore == 100:
        outline(rect2, 3)
    elif maxScore == 150:
        outline(rect3, 3)
    elif maxScore == 200:
        outline(rect4, 3)
    elif maxScore == 250:
        outline(rect5, 3)

    if themeColor == BLUE:
        outline (blueRect, 3)
    elif themeColor == RED:
        outline (redRect,3)
    elif themeColor == GREEN:
        outline (greenRect,3)

    if button == 1:
        if exitRect.collidepoint(mouseX, mouseY) == True:
            state = HOMESTATE
        elif redRect.collidepoint(mouseX, mouseY) == True:
            themeColor = RED
        elif greenRect.collidepoint(mouseX, mouseY) == True:
            themeColor = GREEN
        elif blueRect.collidepoint(mouseX, mouseY) == True:
            themeColor = BLUE
        elif saveRect.collidepoint(mouseX, mouseY) == True:
            state = HOMESTATE
        elif rect1.collidepoint(mouseX, mouseY) == True:
            maxScore = 50
        elif rect2.collidepoint(mouseX, mouseY) == True:
            maxScore = 100
        elif rect3.collidepoint(mouseX, mouseY) == True:
            maxScore = 150
        elif rect4.collidepoint(mouseX, mouseY) == True:
            maxScore = 200
        elif rect5.collidepoint(mouseX, mouseY) == True:
            maxScore = 250
        elif delRect.collidepoint(mouseX,mouseY) == True:
            state = DELSTATE
    return state, themeColor, maxScore

def delete (button, mouseX,mouseY):
    global pwAgain, inputPw, deleted, username, password, secondLogin
    state = DELSTATE
    confirmError=False
    deleteConfirm=False
    find = False
    deleteSuccess = False

    if secondLogin == True:
        username = username1
        password = password1

    draw.rect(screen, PINK, (0, 0, width, height)) 
    pwBox = draw.rect(screen, WHITE, (60, 180, 400, 40))
    backRect = Rect (width//2-120, 300, 240,50)

    string = "%s, this will delete all your data." %username
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(60, 90, textSize[0], textSize[1])
    screen.blit(text, textRect)
    
    string="Please enter your password again to confirm." 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(60, 130, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #delete button
    delRect = draw.rect (screen, WHITE, (width//2-160-70,300,160,50))
    draw.rect (screen, OLDROSE, delRect, 3)
    string = "Delete" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2-200+3, 313, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #cancel 
    cancelRect = draw.rect (screen, WHITE, (width//2+70,300,160,50))
    draw.rect (screen, OLDROSE, cancelRect, 3)
    string = "Cancel" 
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2+107, 313, textSize[0], textSize[1])
    screen.blit(text, textRect)
    
    if delRect.collidepoint(mouseX,mouseY) == True:
        deleteConfirm = True
    if pwBox.collidepoint(mouseX,mouseY):
        inputPw = True
    if inputPw == True:
        draw.rect (screen, OLDROSE,pwBox,2)
    string = pwAgain
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(67, 190, 400, 40)
    screen.blit(text, textRect)  

    if deleteConfirm==True:
        confirmError = False
        try:
            numFile = open ("thing.dat", "r")
            find = True
        except:
            print("No database.")
        numFile = open("thing.dat", "w")
        if find:
            for i in range(0, len(nameList)):
                if nameList[i] == username:
                    if pwList[i] == pwAgain:
                        numFile.write("")
                        deleteSuccess=True
                    else:
                        numFile.write(nameList[i]+"*"+ pwList[i]+"*"+scoreList[i]+"\n")
                        confirmError = True
                else:
                    numFile.write(nameList[i]+"*"+ pwList[i]+"*"+scoreList[i]+"\n")  
            numFile.close() 
    if confirmError == True:
        string = "Wrong password"
        pwAgain=""
        text = fontConS.render(string, 1, OLDROSE)
        textSize = fontConS.size(string)
        textRect = Rect(67, 190, 400, 40)
        screen.blit(text, textRect)  
    
    if deleted == True:
        draw.rect (screen, WHITE, (0,0,width, height))
        string = "Account deleted successfully"
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(width//2-textSize[0]//2, 160, textSize[0], textSize[1])
        screen.blit(text, textRect)
        deleteConfirm = False

        #back to main
        backRect = draw.rect (screen, PINK, (width//2-120, 300, 240,50))
        draw.rect(screen, BLACK, backRect, 2)
        string = "Back to main"
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(width//2-textSize[0]//2, 312, textSize[0], textSize[1])
        screen.blit(text, textRect)

    if button==1:
        if cancelRect.collidepoint(mouseX,mouseY) == True:
            state = SETTINGSTATE
            inputPw = False
        if deleteConfirm==True and deleteSuccess==True:
            deleted = True
        if backRect.collidepoint(mouseX,mouseY) == True and deleted== True:
            state = MAINSTATE
            username=""
            password=""
            inputPw = False
            secondLogin = False
            deleted = False
            pwAgain =""
    return state

def outline (rec, x):
    draw.rect (screen, BLACK, rec, x)

def players (button,mouseX,mouseY):
    global username, password,username1, username2, password1
    
    #choose the number of players
    state=CHOOSESTATE    
    hand=[]
    deck=[]
    secondLogin=False
    draw.rect(screen, PINK, (0, 0, width, height)) 
    drawExit()
    exitRect = Rect(755, 15, 30, 30)

    #write the command for the number of players
    string = "Choose the number of players."
    text = fontConM.render(string, 1, BLACK)
    textSize = fontConM.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 45, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #draw the number boxes
    numBox(1,width//2-115-70, 115)
    numBox(2,width//2+70,115)
    oneRect = Rect (width//2-115-70,210,123,123)
    twoRect = Rect (width//2+70,210,123,123)
    
    if button==3:
        state = HOMESTATE
    if button == 1:
        if exitRect.collidepoint(mouseX, mouseY) == True:
            state = HOMESTATE
        if oneRect.collidepoint(mouseX,mouseY) == True:
            state = SOLITAIRE
            deck = sample (range (1,31),30)
            hand = sample (range (1,31),10)
            for i in range (0, 10):
                deck.remove (hand[i])
            if username2 != "":
                username = username1
        if twoRect.collidepoint(mouseX,mouseY) == True:
            state = LOGINSTATE 
            secondLogin = True
            username1 = username
            password1 = password
            username=""
            password=""
    return state, hand, deck, secondLogin,username1,password1

def numBox (num,x,d):
    boxRect = draw.rect(screen, WHITE, Rect(x, 214, d, d))      #draw the box
    draw.rect(screen, OLDROSE, boxRect, 4)                     #draw the outline
    #write the number
    number = str(num)
    text = fontCon.render(number, 1, BLACK)
    textSize = fontCon.size(number)
    textRect = Rect(x+45, 252, textSize[0], textSize[1])
    screen.blit(text, textRect)

def secondHome (button,mouseX,mouseY):
    global secondLogin, username, password, showCard, turn
    state=SECONDHOME   
    hand1=[]
    hand2=[]
    discardList=[]
    multiDeck=[]   
    draw.rect(screen, PINK, (0, 0, width, height)) 
    drawExit()
    exitRect = Rect(755, 15, 30, 30)

    #round #
    string = "ROUND: "+ str(numRound)
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2-textSize[0]//2, 50, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    #score
    draw.rect(screen, GRAY, (width//2-170, 130, 340, 155)) 
    text = fontConS.render("scoreboard", 1, BLACK)	
    textSize = fontConS.size(string)
    screen.blit (text, Rect (width//2-textSize[0]//2,150,textSize[0], textSize[1]))
    
    text = fontConXs.render(username1 + ": " + str(totalScore1), 1, BLACK)	
    screen.blit(text, Rect(280,205,400,100))  
    text = fontConXs.render(username2 + ": " + str(totalScore2), 1, BLACK)	
    screen.blit(text, Rect(280,240,400,100))  

    #start button
    playRect = draw.rect (screen, WHITE, Rect(width//3, 370, width//3, 52))
    draw.rect (screen, OLDROSE, playRect,3)
    string = "START"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 383, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #rule
    string = "*The player that earns %i points first wins the game." %maxScore
    text = fontConXs.render(string, 1, BLACK)
    textSize = fontConXs.size(string)
    textRect = Rect(width//2 - textSize[0]//2, 450, textSize[0], textSize[1])
    screen.blit(text, textRect)
    if button==1:
        if playRect.collidepoint(mouseX,mouseY)==True:
            state=TWOPLAYER
            multiDeck = sample (range (1, 41), 40)
            hand1 = multiDeck[0:10]      #cards for the first player
            hand2 = multiDeck[10:20]     #cards for the second player
            discardList.append(multiDeck[20])
            multiDeck = multiDeck [21: ]
            showCard=False
            turn = True
        if exitRect.collidepoint(mouseX, mouseY) == True:
            state = HOMESTATE
            secondLogin = False
            username = username1
            password = password1
    if button==3:
        state=HOMESTATE
    return state,hand1,hand2,multiDeck,discardList

def leaderBoard(button,mouseX,mouseY,nameList,pwList,username,password):
    state=LEADERBOARD
    draw.rect(screen,PINK,(0,0,width,height))  
    drawExit()
    exitRect = Rect(755, 15, 30, 30)  
    bigList=[]

    #top players
    string = "TOP PLAYERS"
    text = fontCon.render(string, 1, BLACK)
    textSize = fontCon.size(string)
    textRect = Rect(width//2-textSize[0]//2,40, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    for i in range (0,len(nameList)):
        bigList.append([nameList[i]]+[scoreList[i]])

    for i in range (1, len(bigList)):
        for j in range (0, i):
            if int(bigList[i][1])>=int(bigList[j][1]):
                bigList.insert(j,bigList[i])
                bigList.pop(i+1)
    bigList.pop()
    try:
        for i in range (0,5):
            string = "%i. %s" %(i+1,bigList[i][0])
            text = fontConM.render(string, 1, BLACK)
            textSize = fontConM.size(string)
            textRect = Rect(150,135+55*i, textSize[0], textSize[1])
            screen.blit(text, textRect)  
    except:
        for i in range (0, len(bigList)):
            string = "%i. %s" %(i+1,bigList[i][0])
            text = fontConM.render(string, 1, BLACK)
            textSize = fontConM.size(string)
            textRect = Rect(150,135+55*i, textSize[0], textSize[1])
            screen.blit(text, textRect)  
    if button==1:
        if exitRect.collidepoint(mouseX,mouseY)==True:
            state=HOMESTATE 
    if button==3:
        state=HOMESTATE 
    return state,nameList,pwList
    
def solitaire (button,mouseX,mouseY):    
    global showCard,fromDraw,first
    state=SOLITAIRE     
    draw.rect(screen,PINK,(0,0,width,height))  


    for x in range (1,11):
        #write the scores
        text = fontConXs.render(str(55-5*x) , 1, BLACK)	
        screen.blit(text, Rect(560,65+48*(x-1),100,100))
        draw.line(screen,BLACK,(555,50+48*x),(width-70,50+48*x),2)  

    #draw button
    deckRect=Rect(270,370,100,50)
    draw.rect(screen,WHITE,deckRect) 
    draw.rect(screen, OLDROSE, deckRect, 3)
    string = "DRAW"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(289, 383, textSize[0], textSize[1])
    screen.blit(text, textRect)  

    #deck
    cardRect=Rect(270,200,100,150)      
    draw.rect(screen,BLACK,cardRect,3)        
    text = fontConS.render("card left: %i" %len(deck), 1, BLACK)	
    screen.blit(text, Rect(220,153,400,100))
    
    #give up button
    giveUpRect=Rect(243,490,150,50)  
    draw.rect(screen,WHITE,giveUpRect,)  
    draw.rect(screen, OLDROSE, giveUpRect, 3)     
    text = fontConS.render("GIVE UP", 1, BLACK)	
    screen.blit(text, Rect(263,503,400,100))
    
    for i in range (8, -1,-1):
        if int(hand[i])<int(hand[i+1]):
            score = 5*(9-i)
            draw.rect (screen, WHITE, (70,65,160,50))
            draw.rect (screen, OLDROSE, (70,65,160,50), 3)      #display player's score
            text = fontConS.render("SCORE: %i" %score, 1, BLACK)	
            screen.blit(text, Rect(80,77,400,100)) 
            break
        score = 5*(10-i)

    if score == 50:
        state = SCORESTATE
        first = True
   
    for x in range (0,10):
        i=x     #remember the x value
        x=Rect(625,56+48*x,60,37)       #draw the white rectangles of the rack 
        if themeColor == BLUE:          #set the colour of the box depending on the number
            COLOR1 = (255-3*int(hand[i]),255-3*int(hand[i]),255) 
        elif themeColor == RED:
            COLOR1 = (255, 255-3*int(hand[i]),255-3*int(hand[i])) 
        else:
            COLOR1 = (255-3*int(hand[i]),255,255-3*int(hand[i]))   
        draw.rect(screen,COLOR1,x)
        writeNum(int(i),hand,640)           #write my cards on the rack
        if x.collidepoint(mouseX,mouseY)==True: 
            #if a rectangle is clicked change the card on a rack into a new card
            if int(fromDraw)>0:
                hand[i]=int(fromDraw)
                showCard=False
                fromDraw=0

    if first==True:
        #Draw the first card of a deck at first
        fromDraw=str(deck[0])
        del deck[0]
        showCard=True
        first=False 

    if button==1:
        if deckRect.collidepoint(mouseX,mouseY)==True:
            if len(deck)>0:             #only gets a new card if the deck has more than 0 card
                fromDraw=deck.pop()     #get a new card when the deck button is clicked
                showCard=True           #make it show on the screen
             
            elif len(deck)==0:      
                state=SCORESTATE        #go to the score screen if there is nothing left on deck and the deck button is clicked
                fromDraw=""
                first=True
        elif giveUpRect.collidepoint(mouseX,mouseY)==True:
            #change to the home screen when give up button is clicked
            state=HOMESTATE
            fromDraw=""     #reset the drawn card to nothing
            first=True   

    if showCard==True:
        #draw the drawn card
        if fromDraw != "":
            if themeColor == BLUE:          #set the colour of the box depending on the number
                COLOR2 = (255-3*int(fromDraw),255-3*int(fromDraw),255)
            elif themeColor == RED:
                COLOR2 = (255,255-3*int(fromDraw),255-3*int(fromDraw))
            else:
                COLOR2 = (255-3*int(fromDraw),255, 255-3*int(fromDraw)) 
            draw.rect(screen,COLOR2,cardRect)      #draw the card
        #write the number on the card
        string=str(fromDraw)
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(306, 260, textSize[0], textSize[1])
        screen.blit(text, textRect) 

    if len(deck)==0:
        if fromDraw==0:
            #change to the score screen when there is nothing left on the deck, and when the card is used
            state = SCORESTATE 
            first=True
            fromDraw=""
    return state

def writeNum(x,name, d):       #name is one of the lists 
    #write the cards on the hand on the rack
    text = fontConXs.render(str(name[x]), 1, BLACK)
    textSize = fontConXs.size(str(name[x]))
    textRect = Rect(d, 65+48*x, textSize[0], textSize[1])
    screen.blit(text, textRect) 

def drawScore (button,mouseX,mouseY):
    global calc, sumScore
    state=SCORESTATE    
    draw.rect(screen,PINK,(0,0,width,height))            

    #back button
    string="Back to Main"
    newRect=Rect(width/2-125,420,250,50)
    draw.rect(screen,WHITE,newRect)    
    draw.rect(screen, OLDROSE, newRect, 3)      #outline
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width/2-textSize[0]/2, 432, textSize[0], textSize[1])
    screen.blit(text, textRect)        
    
    for i in range (8, -1,-1):
        if int(hand[i])<int(hand[i+1]):
            score = 5*(9-i)
            break
        score = 5*(10-i)
    try:
        numFile = open ("thing.dat", "w")
        find=True
    except:
        print("No database.")
    if find==True:
        for i in range(0, len(nameList)):
            if username == nameList[i]:
                if calc == True:
                    sumScore = score + int(scoreList[i])
                    calc = False
                numFile.write(username+"*"+pwList[i]+"*"+str(sumScore)+"\n")
                scoreList[i] = str(sumScore)
            else:
                numFile.write(nameList[i]+"*"+pwList[i]+"*"+scoreList[i]+"\n")
        numFile.close() 

    if score == 50:       #player won
        string="YOU WON!"
        text = fontConL.render(string, 1, BLACK)
        textSize = fontConL.size(string)
        textRect = Rect(width/2-textSize[0]/2, 227, textSize[0], textSize[1])
        screen.blit(text, textRect)
        for x in range(0,1):        #win effect
            winEffect(themeColor,250,250)
            time.delay(110)   
            winEffect(BLACK,250,250)
            time.delay(110)
    elif score < 50:       #player lost
        string="YOU LOST."
        text = fontConL.render(string, 1, BLACK)
        textSize = fontConL.size(string)
        textRect = Rect(width/2-textSize[0]/2, 130, textSize[0], textSize[1])
        screen.blit(text, textRect) 
        #write the score
        string2="YOUR SCORE IS %i." %score
        text = fontCon.render(string2, 1, BLACK)
        textSize = fontCon.size(string2)
        textRect = Rect(width/2-textSize[0]/2, 170, textSize[0], textSize[1])
        screen.blit(text, textRect)    
    if newRect.collidepoint(mouseX,mouseY)==True: 
        state = HOMESTATE   #go back to home when the button is clicked
        calc = True
    return state

def winEffect(colour,x,y):
    draw.line(screen,colour, (x+255,y),(x+290,y),5)
    draw.line(screen,colour, (x-5,y),(x+30,y),5)
    draw.line(screen,colour, (x,y-43),(x+45,y-28),5)
    draw.line(screen,colour, (x+250,y-28),(x+285,y-43),5)
    draw.line(screen,colour, (x+50,y-77),(x+75,y-50),5)
    draw.line(screen,colour, (x+215,y-50),(x+240,y-77),5)
    draw.line(screen,colour, (x+113,y-95),(x+121,y-60),5)
    draw.line(screen,colour, (x+169,y-60),(x+177,y-95),5)
    display.flip()

def twoPlayer(button,mouseX,mouseY):  
    global showCard,discarded,deckUse,discardUsed,fromDraw,turn,end,discardList,multiDeck,score1,score2, secondLogin, username
    state=TWOPLAYER     #define the state    
    draw.rect(screen,PINK,(0,0,width,height))  #draw the background
    playerName="" 
    quitRect = Rect (width//2-32,495,64,30)
    draw.line(screen, BLACK, (width//2-32,522),(width//2+32,522),2)
    string = "QUIT"
    text = fontConXs.render(string, 1, BLACK)
    textSize = fontConXs.size(string)
    textRect = Rect(width//2-textSize[0]//2, 500, textSize[0], textSize[1])
    screen.blit(text, textRect)

    for x in range (1,11):
        #write the scores
        text = fontConXs.render(str(55-5*x) , 1, BLACK)	
        screen.blit(text, Rect(655,65+48*(x-1),100,100))
        draw.line(screen,BLACK,(650,50+48*x),(width-20,50+48*x),2) 
        screen.blit(text, Rect(124,65+48*(x-1),100,100))
        draw.line(screen,BLACK,(20,50+48*x),(150,50+48*x),2)               

    #discard button
    discardRect = draw.rect(screen,WHITE,(225,370,130,50))
    draw.rect (screen, OLDROSE, discardRect, 3)
    string = "DISCARD"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(238, 382, textSize[0], textSize[1])
    screen.blit(text, textRect)

    #draw button
    deckRect = draw.rect(screen,WHITE,(455,370,100,50)) 
    draw.rect (screen, OLDROSE, deckRect, 3)    
    string = "DRAW"
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(475, 382, textSize[0], textSize[1])
    screen.blit(text, textRect) 

    cardRect=Rect(455,200,100,150)  #box of the drawn card
    draw.rect (screen, BLACK, cardRect, 3)
    trashRect=Rect(245,200,100,150)  #box of the discarded card 
    draw.rect (screen, BLACK, trashRect, 3)
    
    for i in range (8, -1,-1):
        if int(hand1[i])<int(hand1[i+1]):
            score1 = 5*(9-i)
            scoreRect = draw.rect (screen, WHITE, (650,10,140,37))
            draw.rect (screen, OLDROSE, scoreRect, 2)    
            text = fontConXs.render("SCORE: %i" %score1, 1, BLACK)	
            screen.blit(text, (659,19,100,100)) 
            break
        score1 = 5*(10-i)
    for i in range (8, -1,-1):
        if int(hand2[i])<int(hand2[i+1]):
            score2 = 5*(9-i)
            score2Rect = draw.rect (screen, WHITE, (10,10,140,37))
            draw.rect (screen, OLDROSE, score2Rect, 2)    
            text = fontConXs.render("SCORE: %i" %score2, 1, BLACK)	
            screen.blit(text, (18,19,100,100)) 
            break
        score2 = 5*(10-i)
    if score1==50 or score2 ==50:
        state = MULTISCORESTATE

    if turn==True: 
        playerName = username1
        for x in range (0,10):
            i=x    
            x=Rect(720,56+48*x,50,37)      
            if themeColor == BLUE:          #set the colour of the box depending on the number
                COLOR3 = (255-3*int(hand1[i]),255-3*int(hand1[i]),255) 
            elif themeColor == RED:
                COLOR3 = (255, 255-3*int(hand1[i]),255-3*int(hand1[i])) 
            else:
                COLOR3 = (255-3*int(hand1[i]),255,255-3*int(hand1[i]))   
            draw.rect(screen,COLOR3,x)
            writeNum(int(i),hand1,730)           #write my cards on the rack
            
            if button==1:
                if x.collidepoint(mouseX,mouseY)==True: 
                    if deckUse==True:
                        if int(fromDraw)>0:
                            discardList.append(hand1[i])
                            hand1[i]=int(fromDraw)                   
                            showCard=False
                            fromDraw=0
                            end=True
                    else:
                        if discardUsed==False:
                            old=hand1[i]                   
                            hand1[i]=discardList[-1]                    
                            discardList[-1]
                            discardList.append(old)
                            discardUsed=True   
                            end=True                             
    else:        
        playerName = username2
        for x in range (0,10):
            i=x     #remember the x value
            x=Rect(45,56+48*x,50,37)       #draw the white rectangles of the rack 
            if themeColor == BLUE:          #set the colour of the box depending on the number
                COLOR4 = (255-3*int(hand2[i]),255-3*int(hand2[i]),255) 
            elif themeColor == RED:
                COLOR4 = (255, 255-3*int(hand2[i]),255-3*int(hand2[i])) 
            else:
                COLOR4 = (255-3*int(hand2[i]),255,255-3*int(hand2[i]))   
            draw.rect(screen,COLOR4,x)
            writeNum(int(i),hand2, 55)           #write my cards on the rack

            if button==1:
                if x.collidepoint(mouseX,mouseY)==True:   
                    if deckUse==True:
                        if int(fromDraw)>0:
                            discardList.append(hand2[i])
                            hand2[i]=int(fromDraw)                   
                            showCard=False
                            fromDraw=0
                            end=True
                    else:
                        if discardUsed==False:
                            old=hand2[i]    
                            hand2[i]=discardList[-1]                          
                            discardList[-1]
                            discardList.append(old)
                            discardUsed=True  
                            end=True 
    text = fontConS.render(playerName, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width//2-textSize[0]//2, 50, textSize[0], textSize[1])
    screen.blit(text, textRect) 
 
    if button==1:
        if quitRect.collidepoint(mouseX,mouseY)==True:
            state=HOMESTATE
            secondLogin = False
            username = username1
            fromDraw=""
        if deckRect.collidepoint(mouseX,mouseY)==True:
            if showCard==False:
                if len(multiDeck)>0:
                    fromDraw=multiDeck.pop()                  
                    showCard=True
                    deckUse=True
        elif discardRect.collidepoint(mouseX,mouseY)==True:
            if int(fromDraw)>0:
                discarded=True
                showCard=False
                discardList.append(fromDraw)
                fromDraw=0
                end=True
        elif trashRect.collidepoint(mouseX,mouseY)==True:
            if int(fromDraw)==0:
                discardUsed=False
                deckUse=False
        elif cardRect.collidepoint(mouseX,mouseY)==True:
            deckUse=True
    if deckUse==True:
        draw.rect(screen,OLDROSE,cardRect,3)
    if deckUse==False:
        draw.rect(screen,OLDROSE,trashRect,3)    
    if showCard==True:
        draw.rect(screen,WHITE,cardRect)
        string=str(fromDraw)
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(490, 260, textSize[0], textSize[1])
        screen.blit(text, textRect)
    if discarded==True:
        draw.rect(screen,WHITE,trashRect)
        string=str(discardList[-1])
        text = fontConS.render(string, 1, BLACK)
        textSize = fontConS.size(string)
        textRect = Rect(281, 260, textSize[0], textSize[1])
        screen.blit(text, textRect) 
    if end==True:
        if turn==True:
            turn=False
        else:
            turn=True
        end=False
    if len(multiDeck)==0:
        if fromDraw==0:
            #change to the score screen when there is nothing left on the deck, and when the card is used
            state = MULTISCORESTATE 
            fromDraw=""
            showCard=False

    text = fontConXs.render("card left: %i" %len(multiDeck), 1, BLACK)	#display the number of card left in the deck
    screen.blit(text, Rect(427,170,400,100))  

    return state,score1, score2

def multiScore (button,mouseX,mouseY):
    global totalScore1,totalScore2, calculate, numRound, add1, add2,sumScore1, sumScore2
    gameEnd = False
    state=MULTISCORESTATE
    draw.rect(screen,PINK,(0,0,width,height))
    
    #play again button
    string = "Next Round"
    againRect = draw.rect(screen,WHITE,(135,420,230,50)) 
    draw.rect(screen, OLDROSE, againRect, 3)      #outline      
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(173, 432, textSize[0], textSize[1])
    screen.blit(text, textRect)  

    #back button
    string="Back to Main"
    backRect=Rect(width-365,420,230,50)
    draw.rect(screen,WHITE,backRect)    
    draw.rect(screen, OLDROSE, backRect, 3)      #outline
    text = fontConS.render(string, 1, BLACK)
    textSize = fontConS.size(string)
    textRect = Rect(width-365+28, 432, textSize[0], textSize[1])
    screen.blit(text, textRect)    

    if calculate == True:
        totalScore1+=score1
        totalScore2+=score2
        calculate = False

    #score
    draw.rect(screen, GRAY, (width//2-170, 150, 340, 155))  
    text = fontConS.render("scoreboard", 1, BLACK)	
    textSize = fontConS.size(string)
    screen.blit (text, Rect (width//2-textSize[0]//2,170,textSize[0], textSize[1]))
    
    text = fontConXs.render(username1 + ": " + str(totalScore1), 1, BLACK)	
    screen.blit(text, Rect(280,225,400,100))  
    text = fontConXs.render(username2 + ": " + str(totalScore2), 1, BLACK)	
    screen.blit(text, Rect(280,260,400,100))  
    
    if totalScore2>=maxScore or totalScore1>=maxScore:
        if score1>score2:
            winnerText = username1 + " WON THE GAME!"          
        elif score1<score2:
            winnerText = username2 + " WON THE GAME!"       
        else:
            winnerText="TIE!"
        gameEnd = True
        text = fontConS.render(winnerText, 1, BLACK)
        textSize = fontConS.size(winnerText)
        screen.blit(text, Rect(width//2-textSize[0]//2, 80, textSize[0], textSize[1]))   #write who one the game
    else:
        if score1 > score2:
            winString =  username1 + " won this round."
        elif score1 < score2:
            winString = username2 + " won this round."
        elif score1 == score2:
            winString = "This round was a tie."
        text = fontConS.render(winString, 1, BLACK)
        textSize = fontConS.size(winString)
        screen.blit(text, Rect(width//2-textSize[0]//2, 80, textSize[0], textSize[1]))  
    if gameEnd == True:
        draw.rect (screen, PINK, (0,height//2,width, height//2))
        endRect = draw.rect(screen, WHITE, (width//2-170, 480, 340, 155))  
        text = fontConS.render("BACK TO MAIN", 1, BLACK)	
        textSize = fontConS.size(string)
        screen.blit (text, Rect (width//2-textSize[0]//2,495,textSize[0], textSize[1]))
    
    if button==1:
        if againRect.collidepoint(mouseX,mouseY)==True: 
            state = SECONDHOME      #start a new round when the button is clicked
            numRound+=1             #increase the round number by 1 
            calculate=True
        if gameEnd == True and endRect.collidepoint(mouseX,mouseY)==True:
            numRound = 1
            state = HOMESTATE
            calculate = True
        if backRect.collidepoint(mouseX,mouseY)==True:
            state=HOMESTATE
            numRound = 1
            calculate = True
            try:
                numFile = open ("thing.dat", "w")
                find=True
            except:
                print("No database.")
            if find==True:
                for i in range(0, len(nameList)):
                    if username1 == nameList[i]:
                        if add1 == True:
                            sumScore1 = totalScore1 + int(scoreList[i])
                            add1 = False
                        numFile.write(username1+"*"+pwList[i]+"*"+str(sumScore1)+"\n")
                        scoreList[i] = str(sumScore1)
                    elif username2 == nameList[i]:
                        if add2 == True:
                            sumScore2 = totalScore2 + int(scoreList[i])
                            add2 = False
                        numFile.write(username2+"*"+pwList[i]+"*"+str(sumScore2)+"\n")
                        scoreList[i] = str(sumScore2)
                    else:
                        numFile.write(nameList[i]+"*"+pwList[i]+"*"+scoreList[i]+"\n")
                numFile.close() 
    return state,numRound

#variables
registered=False
running = True
menuState = MAINSTATE
myClock = time.Clock()
button = mx = my = 0
menuState = MAINSTATE
username = ""
password=""
userInput = ""
entered = False
pwIn = False
usernameIn=False
exist = False
error1 = False
error2 = False
find=False
multiple=False
discarded=True
deckUse=True
showCard=False
fromDiscard=0
fromDraw=0
username2=""
password2=""
discardUsed=True
playerName=""
turn=True     
end=False  
nameList=[]
pwList=[]
scoreList=[]
card=[]
secondLogin=False
firstDiscard=0
first=True  
numRound=1
username1=""
password1=""
score1=0
score2=0
calculate=True
themeColor = BLUE
totalScore1 = 0
totalScore2 = 0
add1 = True
add2 = True
sumScore1=0
sumScore2=0
calc = True
sumScore=0
discardList=[]
bigList=[]
maxScore = 100
pwAgain=""
inputPw = False
deleteConfirm = False
confirmError = False
deleted = False

# Game Loop
while running:
    button = 0
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos          
            button = evnt.button
        if evnt.type == KEYDOWN:
            if menuState==LOGINSTATE or menuState==REGISTERSTATE or menuState==DELSTATE:
                if key.name(evnt.key) == "backspace":
                    if pwIn==True:
                        password = password[:-1] 
                    elif inputPw==True:
                        pwAgain = pwAgain[:-1]
                    else:
                        username = username[:-1]                     
                elif key.name(evnt.key) == "space":
                    if pwIn==True:
                        password+=" " 
                    elif inputPw==True:
                        pwAgain+= " "
                    else:
                        username+=" "                                          
                elif len(key.name(evnt.key)) > 1:
                    print("Invalid character.")
                else:
                    if pwIn==True:
                        password+=key.name(evnt.key)
                    elif inputPw==True:
                        pwAgain+=key.name(evnt.key)
                    else:
                        username+=key.name(evnt.key)  
                           
    if menuState == MAINSTATE:   
        menuState = mainMenu(button, mx, my)
    elif menuState == HOMESTATE:
        menuState = drawHome(button,mx,my)
    elif menuState == CHOOSESTATE:
        menuState, hand, deck, secondLogin,username1,password1=players(button, mx, my)
    elif menuState == SOLITAIRE:
        menuState = solitaire(button, mx, my)   
    elif menuState == SCORESTATE:
        menuState=drawScore(button, mx, my) 
    elif menuState == TWOPLAYER: 
        menuState,score1, score2=twoPlayer(button,mx,my) 
    elif menuState == LOGINSTATE:         
        menuState,entered,pwIn,usernameIn,username2,password2,nameList,pwList,scoreList,username1,password1=drawLogin(button, mx, my,nameList,pwList,scoreList)
    elif menuState == REGISTERSTATE:       
        menuState,entered,pwIn,usernameIn=drawRegister(button, mx, my)  
    elif menuState == MULTISCORESTATE:
        menuState,numRound=multiScore(button,mx,my)
    elif menuState == SECONDHOME:
        menuState,hand1,hand2,multiDeck,discardList=secondHome(button,mx,my)
    elif menuState == LEADERBOARD:
        menuState,nameList,pwList=leaderBoard(button,mx,my,nameList,pwList,username,password)
    elif menuState == HELPSTATE:
        menuState = help (button, mx, my)
    elif menuState == SETTINGSTATE:
        menuState, themeColor,maxScore = setting (button, mx, my)
    elif menuState == DELSTATE:
        menuState = delete (button, mx,my)
    else:
        running = False
    myClock.tick(60)                     # waits long enough to have 60 fps
    display.flip()  

quit()