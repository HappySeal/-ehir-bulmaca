import pygame,random,sys,time

pygame.init()

displayW = 1579
displayH = 900
infoObject = pygame.display.Info()

scale = 1

cityName = ["Edirne","Kırklareli","Tekirdağ","İstanbul","Kocaeli","Yalova","Sakarya","Düzce","Zonguldak","Bartın","Kastamonu","Sinop","Samsun","Ordu","Giresun","Trabzon","Rize","Artvin","Ardahan","Erzurum","Bayburt","Gümüşhane","Sivas","Tokat","Amasya","Çorum","Çankırı","Bolu","Bilecik","Balıkesir","Çanakkale","İzmir","Manisa","Kütahya","Eskişehir","Ankara","Kırıkkale","Yozgat","Erzincan","Kars","Ağrı","Iğdır","Van","Hakkari","Şirnak","Siirt","Bitlis","Muş","Bingöl","Diyarbakır","Mardin","Şanlıurfa","Adıyaman","Elazığ","Tunceli","Malatya","Kahramanmaraş","Gaziantep","Batman","Kayseri","Adana","Osmaniye","Hatay","Nevşehir","Niğde","Mersin","Karaman","Konya","Aksaray","Kilis","Antalya","Isparta","Afyonkarahisar","Uşak","Denizli","Muğla","Aydin","Bursa","Kırşehir","Karabük","Burdur"]
#print(len(cityName))
    

black = (0,0,0)
white = (255,255,255)

lastTime = time.time()

Sure = 0
trueAnswer = 0
score = 0
wrong = 0
correct = 0
reason = 0
Ispaused = False

citySize = 0
cityImg = pygame.image.load("Sehirler/1.png")
cityRandom = 0
city = ""

HIscore = 0

gameDisplay = pygame.display.set_mode((int(displayW*scale),int(displayH*scale)))
pygame.display.set_caption("Sehir Bulmaca")
clock = pygame.time.Clock()



true = pygame.mixer.Sound("True.wav")
false = pygame.mixer.Sound("False.wav")

button1 = pygame.image.load("Buttons/b1.png")
button2 = pygame.image.load("Buttons/b2.png")
button3 = pygame.image.load("Buttons/b3.png")
button4 = pygame.image.load("Buttons/b4.png")
pauseImg = pygame.image.load("Buttons/p1.png")

defaultButton1 = pygame.Surface.get_size(button1)
defaultButton2 = pygame.Surface.get_size(button2)
defaultButton3 = pygame.Surface.get_size(button3)
defaultButton4 = pygame.Surface.get_size(button4)

defaultPause = pygame.Surface.get_size(pauseImg)

def cityDisplay(x,y,path):
    global citySize
    global cityImg
    cityImg = pygame.image.load(path)
    citySize = pygame.Surface.get_size(cityImg)
    cityImg = pygame.transform.smoothscale(cityImg,(int(citySize[0]*scale),int(citySize[1]*scale)))
    #print(type(cityImg))

    gameDisplay.blit(cityImg,(x,y))

def PauseDisplay(x,y):
    global pauseImg,scale
    pauseImg = pygame.transform.smoothscale(pauseImg,(int(defaultPause[0]*scale),int(defaultPause[1]*scale)))
    gameDisplay.blit(pauseImg,(x,y))

def button1Display(x,y):
    global button1,scale
    button1 = pygame.transform.smoothscale(button1,(int(defaultButton1[0]*scale),int(defaultButton1[1]*scale)))
    gameDisplay.blit(button1,(x,y))

def button2Display(x,y):
    global button2,scale
    button2 = pygame.transform.smoothscale(button2,(int(defaultButton2[0]*scale),int(defaultButton2[1]*scale)))
    gameDisplay.blit(button2,(x,y))

def button3Display(x,y):
    global button3,scale
    button3 = pygame.transform.smoothscale(button3,(int(defaultButton3[0]*scale),int(defaultButton3[1]*scale)))
    gameDisplay.blit(button3,(x,y))

def button4Display(x,y):
    global button4,scale
    button4 = pygame.transform.smoothscale(button4,(int(defaultButton4[0]*scale),int(defaultButton4[1]*scale)))
    gameDisplay.blit(button4,(x,y))

def text_objects(text,font,color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def all_display(text,color):
    normalText = pygame.font.Font("font.ttf",30)
    TextSurf , TextRect = text_objects(text,normalText,color)
    TextRect.center = (180,30)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def message_display(text,x,y,color):
    normalText = pygame.font.Font("font.ttf",30)
    TextSurf , TextRect = text_objects(text,normalText,color)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def pauseScreen():
    global scale
    #print(scale)
    gameDisplay.fill(black)

    message_display("OYUN DURDURULDU..",(displayW/2)*scale,((displayH/2)-150)*scale,white)

    button3Display((((displayW/2)-((defaultButton3[0])/2))*scale),(((displayH/2))*scale))
    message_display("DEVAM ET",((displayW/2)*scale),(((displayH/2)+(defaultButton3[1]/2))*scale),white)

    button2Display((((displayW/2)-((defaultButton2[0])/2))*scale),(((displayH/2)+120)*scale))
    message_display("OYUNDAN ÇIK",(((displayW/2))*scale),((((displayH/2)+120+defaultButton2[1]/2))*scale),white)

def newMap():
    global trueAnswer
    global cityRandom
    global city
    global reason
    global scale

    print("*"*20,"\n")
    gameDisplay = pygame.display.set_mode((int(displayW*scale),int(displayH*scale)))
    cityRandom = random.randint(1,81)
    city = "Sehirler/"+str(cityRandom)+".png"
    #print("Şehir Adi : " + cityName[(cityRandom-1)])
    #print("File Name: ",city)
    buttonText = ["","","",""]
    for i in range(0,4):
        answerRandom = random.randint(0,80)
        while answerRandom == cityRandom-1:
            answerRandom = random.randint(0,80)
        for z in range(0,4):
            try:
                while buttonText[z] == cityName[(answerRandom-1)]:
                    answerRandom = random.randint(0,80)

            except:
                pass

        print("Random:",answerRandom,"  True:",cityRandom)

        buttonText[i] = cityName[(answerRandom)]
        i+=1
    trueAnswer = random.randint(0,3)
    buttonText[trueAnswer] = cityName[(cityRandom-1)]

    cityDisplay(0,0,city)

    PauseDisplay(12*scale,12*scale)

    button1Display(0*scale,678*scale)
    message_display(buttonText[0],(displayW/4)*scale,733*scale,white)

    button2Display((displayW/2)*scale,678*scale)
    message_display(buttonText[1],(displayW/4*3)*scale,733*scale,white)

    button3Display(0*scale,789*scale)
    message_display(buttonText[2],(displayW/4)*scale,844*scale,white)

    button4Display((displayW/2)*scale,789*scale)
    message_display(buttonText[3],(displayW/4*3)*scale,844*scale,white)



def pause():
    global Ispaused,Sure

    pauseScreen()

    while Ispaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #(((displayW/2)-((defaultButton2[0])/2))*scale),(((displayH/2)+120)*scale)
        if (((displayW/2)-((defaultButton3[0])/2))*scale) < mouse[0] < (((displayW/2)+((defaultButton3[0])/2))*scale) and (displayH/2)*scale < mouse[1] < ((displayH/2)+defaultButton3[1])*scale:
            if click[0] == 1:
                Ispaused = False
        if (((displayW/2)-((defaultButton2[0])/2))*scale) < mouse[0] < (((displayW/2)+((defaultButton2[0])/2))*scale) and ((displayH/2)+120)*scale < mouse[1] < ((displayH/2)+120+defaultButton2[1])*scale:
            if click[0] == 1:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)

def endWindow():
    gameExit = False
    global score,correct,wrong
    global cityImg
    global reason
    global HIscore
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        score = correct - wrong
        if reason == 1:
            message_display("SÜRENİZ BİTTİ  ! ",(displayW/2)*scale,(displayH/2)*scale,white)
            time.sleep(0.5)
            message_display("Doğru Sayınız  : "+str(correct),(displayW/2)*scale,((displayH/2)+70)*scale,white)
            time.sleep(0.5)
            message_display("Yanlış  Sayınız : "+str(wrong),(displayW/2)*scale,((displayH/2)+150)*scale,white)
            time.sleep(0.5)
            message_display("Toplam Puan   : "+str(score),(displayW/2)*scale,((displayH/2)+220)*scale,white)
 
        
        if HIscore < score:
            HIscore = score
            message_display("YENİ YÜKSEK PUAN !",(displayW/2)*scale,((displayH/2)-100)*scale,white)
            true.play()
            time.sleep(0.1)
            true.play()
            time.sleep(0.1)
            true.play()
            time.sleep(0.1)
            true.play()
        score = 0
        correct = 0
        wrong = 0
        
        click = pygame.mouse.get_pressed()

        time.sleep(3)
        reason = 0
        game_loop()
        pygame.display.update()
        clock.tick(60)


def game_loop():
    gameExit = False

    newMap()


    global scale
    global score,correct,wrong
    global cityImg
    global city
    global reason
    global Ispaused
    global Sure



    lastTime = time.time()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    newMap()
                    PauseDisplay(129*scale,20*scale)

                if event.key == pygame.K_1:
                    scale = 0.9


                if event.key == pygame.K_2:
                    scale = 0.8


                if event.key == pygame.K_3:
                    scale = 0.7


                if event.key == pygame.K_0:
                    scale = 1

                if event.key == pygame.K_9:
                    scale = (infoObject.current_w/displayW)

                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #print(mouse)

        gameDisplay.blit(cityImg,(0,0))
        gameDisplay.blit(pauseImg,(12*scale,12*scale))

        Sure = 120-int(time.time()-lastTime)

        score = correct - wrong
            
        message_display(("Puanınız : "+str(score)),1450*scale,20*scale,black)
        message_display(("Süre : "+str(Sure)),1450*scale,70*scale,black)


        if 12*scale < mouse[0] < 76*scale and 12*scale < mouse[1] < 76*scale:
            if click[0] == 1:
                Ispaused = True
                pause()
                newMap()

        if Sure == 0:
            reason = 1
            endWindow()

        if 0*scale < mouse[0] < (displayW/2)*scale and 678*scale < mouse[1] < 788*scale:
            if click[0] == 1:
                if trueAnswer == 0:
                    true.set_volume(.5)
                    true.play()
                    newMap()
                    correct+=1
                    #print(score)
                else:
                    false.set_volume(.5)
                    false.play()
                    newMap()
                    wrong+=1
        if (displayW/2)*scale < mouse[0] < (displayW)*scale and 678*scale < mouse[1] < 788*scale:
            if click[0] == 1:
                if trueAnswer == 1:
                    true.set_volume(.5)
                    true.play()
                    newMap()
                    correct+=1
                    #print(score)
                else:
                    false.set_volume(.5)
                    false.play()
                    newMap()
                    wrong+=1
        if 0*scale < mouse[0] < (displayW/2)*scale and 788*scale < mouse[1] < displayH*scale:
            if click[0] == 1:
                if trueAnswer == 2:
                    true.set_volume(.5)
                    true.play()
                    newMap()
                    correct+=1
                    #print(score)
                else:
                    false.set_volume(.5)
                    false.play()
                    newMap()
                    wrong+=1
        if (((displayW/2)*scale) < mouse[0] < displayW) and (788*scale < mouse[1] < displayH*scale):
            if click[0] == 1:
                #print(trueAnswer)
                if trueAnswer == 3:
                    true.set_volume(.5)
                    true.play()
                    newMap()
                    correct+=1
                    #print(score)
                else:
                    false.set_volume(.5)
                    false.play()
                    newMap()
                    wrong+=1
        pygame.display.update()
        clock.tick(30)
game_loop()

