#!/usr/bin/env python
# coding: utf-8

# # 01/12/2022
# 
# # Computer Vision
# 
# # Virtual Calculator
# 
# # Muallif: Farrux Sotivoldiyev

# In[3]:


get_ipython().system('pip install cvzone')


# In[1]:


get_ipython().system('pip install mediapipe')


# In[1]:


import cv2
from cvzone.HandTrackingModule import HandDetector


# In[2]:


class Button:
    def __init__(self,pos,width,height,value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
        
    def draw(self,img):
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(255,255,255),cv2.FILLED)
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
        cv2.putText(img,self.value,(self.pos[0]+40,self.pos[1]+60),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)
        
    def checkClick(self,x,y):
        if self.pos[0]<x<self.pos[0]+self.width and self.pos[1]<y<self.pos[1]+self.height:
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(255,255,255),cv2.FILLED)
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
            cv2.putText(img,self.value,(self.pos[0]+20,self.pos[1]+70),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)
            return True
        else:
            return False
            


# In[ ]:


# Webcamera
video = cv2.VideoCapture(0)
video.set(3,1080) # with
video.set(4,720) # heigh
detector = HandDetector(detectionCon=0.8,maxHands=1)



# Button yaratish
buttonListValue = [['7','8','9','*'],
                   ['4','5','6','-'],
                   ['1','2','3','+'],
                   ['0','/','.','=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x*100 + 800
        ypos = y*100 + 150
        buttonList.append(Button((xpos,ypos ),100,100,buttonListValue[y][x]))

        
        
#o'zgrauvchilar
myEquation = ''
delayCounter = 0


# Tsikl
while True:
    kadr,img = video.read()
    img = cv2.flip(img,1)
    
    # Qo'lni aniqlash
    hands, img = detector.findHands(img,flipType=False)
    
    
    # Barcha tugmalarni chizish
    cv2.rectangle(img,(800,50),(800+400,70+100),(255,255,255),cv2.FILLED)
    cv2.rectangle(img,(800,50),(800+400,70+100),(50,50,50),3)
    
        
    for button in buttonList:
        button.draw(img)
        
    # Qo'lni tekshiring
    if hands:
        lmList = hands[0]['lmList']
        length, info, img = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)
        x,y = lmList[8][0:2]
        if length<50:
            for i,button in enumerate(buttonList):
                if button.checkClick(x,y) and delayCounter==0:
                    myValue = buttonListValue[int(i%4)][int(i/4)]
                    if myValue == "=":
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += myValue
                    delayCounter = 1
                             
    # Takrorlashdan saqlanish
    if delayCounter != 0:
        delayCounter += 1 
        if delayCounter>10:
            delayCounter = 0

    # Natijani ko'rsatish
    cv2.putText(img,myEquation,(810,120),cv2.FONT_HERSHEY_PLAIN,3,(50,50,50),3)    
     
    
   # tasvir ko'rinishi
    cv2.imshow("Virtual Kankulyator by Farruxbek", img)
    key = cv2.waitKey(1)
    if key==ord("c"):
        myEquation = "" 


# In[ ]:





# In[ ]:





# In[ ]:




