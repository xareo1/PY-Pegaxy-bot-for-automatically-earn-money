# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:08:58 2021

@author: vndlz
"""

import pyautogui
import keyboard
import time

def racer():
  pyautogui.leftClick(1326,874)
  pyautogui.leftClick(896,1060)
  time.sleep(0.3)
  pyautogui.leftClick(1823,548)
  pyautogui.leftClick(1038,620)
  pyautogui.leftClick(774,983)
  pyautogui.leftClick(958,590)
  pyautogui.leftClick(1629,615)
  time.sleep(3.75)

def horseRent():
 #click to horse
 pyautogui.leftClick(369,494)
 time.sleep(0.5)
 #click to first rent
 pyautogui.leftClick(1621,970)
 #click to second rent
 pyautogui.leftClick(952,594)
 
 
i=0
while i<10:
 if keyboard.is_pressed('1'):
  i = 1;
  while i == 1:
   print("racing")
   racer()
   if keyboard.is_pressed('3'):
     break;
 if keyboard.is_pressed('2'):
  print("horse renting")
  horseRent()
 if keyboard.is_pressed('3'):
  print("idle mode")
  time.sleep(0.25)
 if keyboard.is_pressed('4'):
  print("exiting")
  break;
