#!/usr/bin/env python
# coding: utf-8

# # 02/12/2022
# 
# # Computer Vision
# 
# # Yuz_va_kozni_topish(haarcascade modellaridan foydalanib)
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


face = cv2.CascadeClassifier("C:/Users/farru/ai/MODELLAR/haarcascades/haarcascade_frontalface_alt.xml")
eye = cv2.CascadeClassifier("C:/Users/farru/ai/MODELLAR/haarcascades/haarcascade_eye_tree_eyeglasses.xml")

video = cv2.VideoCapture(0)

while video.isOpened():
    i,kadr = video.read()
    
    if not i:
        break
        
    koz = eye.detectMultiScale(kadr,minSize=(0,0),maxSize=(50,50))
    yuz = face.detectMultiScale(kadr,minSize=(100,100),maxSize=(500,500))
    yuz_copy = kadr.copy()
    
    for x,y,w,h in koz:
        cv2.rectangle(yuz_copy,(x,y),(x+w,y+h),(255,0,0),3)
        
    for x,y,w,h in yuz:
        cv2.rectangle(yuz_copy,(x,y),(x+w,y+h),(255,0,0),3)
        
    cv2.imshow("Farruxbek",yuz_copy)
        
    if cv2.waitKey(40) & 0XFF==ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()


# In[ ]:




