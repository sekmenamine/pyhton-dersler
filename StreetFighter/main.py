#pgzero
import random
import time


HEIGHT=1200
IMAGE_HEIGHT=600
WIDTH=1000
FPS=30
TITLE="The Original Road Fighter"

#actors
logo=Actor("Street_Fighter_logo",(500,500))
play_buton=Actor("play_button2",(500,800))
exit=Actor("exit2",(930,50))

koleksiyon_buton=Actor("collection_button",(500,1000))
koleksiyon_yuvarlak1=Actor("collections",(225,670))
koleksiyon_yuvarlak2=Actor("collections",(525,670))
koleksiyon_yuvarlak3=Actor("collections",(825,670))

#cars
turuncu_araba=Actor("araba-turuncu",(227,615))
mor_araba=Actor("araba-mor",(527,615))
mavi_araba=Actor("araba-mavi",(827,615))

#ticks
tick1=Actor("tick-small2",(525,-50723))


yol1=Actor("yol_bg", (500,IMAGE_HEIGHT))
yol2=Actor("yol_bg", (500,-IMAGE_HEIGHT))
yol_hiz = 8
yol_sag=310
yol_sol=700


araba=Actor("araba", (495,1000))
araba_hiz = 5
dusman_arabalar = []
koleksiyon = []
dusman_araba_hiz=10
mod = 'menu'
puan=300

#loop cars
def yeni_dusman(y):
    x = random.randint(yol_sag,yol_sol)
    araba_yesil=Actor("araba-yesil", (x,-50-y*250))
    dusman_arabalar.append(araba_yesil)

for i in range(5):
    yeni_dusman(i)

#first draw
def draw():
    global mod, puan, araba

    screen.fill("black")
    screen.draw.text("POINT:", center = (50, 50), color = "white", fontsize = 20)
    screen.draw.text(puan, center = (50, 80), color = "white", fontsize = 20) 


    if mod == 'oyun':
        yol1.draw()
        yol2.draw()
        araba.draw()
        exit.draw()
        for i in range(len(dusman_arabalar)):
            dusman_arabalar[i].draw()

    elif mod=="end":
        screen.draw.text("YOU", center = (400, 500), color = "red", fontsize = 200)
        screen.draw.text("LOST!", center = (500, 800), color = "red", fontsize = 200) 
        for i in range(len(dusman_arabalar)):
            dusman_arabalar[i].x = random.randint(yol_sag,yol_sol)
            dusman_arabalar[i].y=-50-i*250

    elif mod=="menu":
        logo.draw()
        play_buton.draw()
        koleksiyon_buton.draw()
        screen.draw.text("SHOP", center = (500, 993), color = "#EBB24F", fontsize = 50, italic=True)
    
    elif mod == "mağaza":
        koleksiyon_yuvarlak1.draw()
        koleksiyon_yuvarlak2.draw()
        koleksiyon_yuvarlak3.draw()
        screen.draw.text("100$", center = (225,783), color = "#BA9652", fontsize = 30, italic=True)
        screen.draw.text("150$", center = (525, 783), color = "#BA9652", fontsize = 30, italic=True)
        screen.draw.text("200$", center = (825, 783), color = "#BA9652", fontsize = 30, italic=True)
        turuncu_araba.draw()
        mor_araba.draw()
        mavi_araba.draw()
        exit.draw()
        tick1.draw()
        
#update draw
def update(dt):
    global mod, puan, araba
        
    if mod=="end":
        time.sleep(3)
        #puan=0
        mod="menu"
            
    if mod =="oyun":
    
        if (keyboard.left or keyboard.a) and araba.x > yol_sag:
    	    araba.x-=araba_hiz
            
        if (keyboard.right or keyboard.d) and araba.x < yol_sol:
            araba.x+=araba_hiz
        
        #arkaplanları hareket ettirir
        yol1.y+=yol_hiz
        yol2.y+=yol_hiz
        

        #eğer arkaplanlar ekranın dışına çıkarsa en başa al
        if yol1.y>HEIGHT*1.5:
            yol1.y=-IMAGE_HEIGHT+yol_hiz
        if yol2.y>HEIGHT*1.5:
            yol2.y=-IMAGE_HEIGHT+yol_hiz
            
        for i in range(len(dusman_arabalar)):
            dusman_arabalar[i].y+=dusman_araba_hiz
    
            if dusman_arabalar[i].y>HEIGHT:
                dusman_arabalar.pop(i)
                yeni_dusman(0)
                puan+=1
    
            elif araba.colliderect(dusman_arabalar[i]):
                mod="end"
                break
    
    
        
def on_mouse_down(button,pos):
    global mod,puan
    
    if button == mouse.left and mod =="menu" and play_buton.collidepoint(pos):
        mod="oyun"
    
    if button == mouse.left and mod =="oyun" and exit.collidepoint(pos):
        mod="menu"
        for i in range(len(dusman_arabalar)):
            dusman_arabalar[i].x = random.randint(yol_sag,yol_sol)
            dusman_arabalar[i].y=-50-i*250

    if button == mouse.left and mod =="menu" and koleksiyon_buton.collidepoint(pos):
        mod="mağaza"

    if button == mouse.left and mod =="mağaza" and exit.collidepoint(pos):
        mod="menu"



    if button == mouse.left and mod =="mağaza" and koleksiyon_yuvarlak1.collidepoint and turuncu_araba.collidepoint(pos):
        if turuncu_araba not in koleksiyon:
            if puan>100:
                araba.image="araba-turuncu"
                dusman_araba_hiz=7
                puan-=100
                koleksiyon.append(turuncu_araba)
                turuncu_araba.y=500
                animate(turuncu_araba,tween="bounce_end",duration=1,y=615)
              
        if turuncu_araba in koleksiyon:
            araba.image="araba-turuncu"
            turuncu_araba.y=500
            animate(turuncu_araba,tween="bounce_end",duration=1,y=615)
        tick1.pos=(270,540)

            
    if button == mouse.left and mod =="mağaza" and koleksiyon_yuvarlak2.collidepoint and mor_araba.collidepoint(pos):
        if mor_araba not in koleksiyon:
            if puan>150:
                araba.image="araba-mor"
                dusman_araba_hiz=9
                puan-=150
                koleksiyon.append(mor_araba)
                mor_araba.y=500
                animate(mor_araba,tween="bounce_end",duration=1,y=615)
                
        if mor_araba in koleksiyon:
            araba.image="araba-mor"
            mor_araba.y=500
            animate(mor_araba,tween="bounce_end",duration=1,y=615)
            
        tick1.pos=(570,540)
        
    if button == mouse.left and mod =="mağaza" and koleksiyon_yuvarlak3.collidepoint and mavi_araba.collidepoint(pos):
        if mavi_araba not in koleksiyon:
            if puan>=200:
                araba.image="araba-mavi"
                dusman_araba_hiz=12
                puan-=200
                koleksiyon.append(mavi_araba)
                mavi_araba.y=500
                animate(mavi_araba,tween="bounce_end",duration=1,y=615)

        if mavi_araba in koleksiyon:
            araba.image="araba-mavi"
            mavi_araba.y=500
            animate(mavi_araba,tween="bounce_end",duration=1,y=615)

        tick1.pos=(870,540) 

    
