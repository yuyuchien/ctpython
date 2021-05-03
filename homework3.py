# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:37:27 2021

@author: user
"""
import random

ans = random.randint(1,100) 
guess = 0
i = 0
while ans != guess:
    guess = int (input('輸入 1-100問整數猜數:'))
    i +=1
    if guess > ans:
        print('猜小一點','-',guess)
    if guess < ans:
        print('猜大一點',guess,'-')
    if i == 5:
        break
if ans == guess:
    print('答對了!')
else:
    print ('答錯五次!請重新挑戰')