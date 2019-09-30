# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:13:29 2019

@author: Natalia
"""

from random import randint, choice
import sys

class Player:
    def __init__(self,points,a,b,c,d):
        self.points = points
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def healing(self):
        healed_points=randint(self.a,self.b)
        self.points += healed_points
        print('healing: + ', healed_points,' points')
        
    def small_injury(self):
        kick = randint(self.a,self.b)
        if self.points-kick<=0:
            self.points=0
        else:
            self.points -= kick
        print('kicked out ',kick,' points')
        
    def big_injury(self):
        kick = randint(self.c,self.d)
        self.points -= randint(self.c,self.d)
        if self.points-kick<=0:
            self.points=0
        else:
            self.points -= kick
        print('kicked out ',kick,' points')
    
    def action(self,num): # pick the action to execute
        if num == 1:
            return self.healing()
        elif num == 2:
            return self.small_injury()
        else:
            return self.big_injury()

# bounderies for small injury
a = 5
b = 15
# bounderies for big injury
c = 20
d = 30
# max number of points at start
bound = 1000
# tries for incorrect input of points by user
tries=0
points = input('Введите начальное количество очков у игроков (<='+str(bound)+'): ')
while True:
    try:
        points = int(points)
        if points<=bound:
            break
        else:
            tries+=1
            points = input('Введите начальное количество очков у игроков (<=1000): ')
    except:
        tries+=1
        points = input('Введите начальное количество очков у игроков (<=1000): ')
    if tries>=6:
        sys.exit(0)
     
me = Player(points,a,b,c,d) 
computer = Player(points,a,b,c,d)
i = 0
print('You have ',points)
print('Computer has ', points)
print('\n\n')
while me.points>0 and computer.points>0:
    i +=1
    if i%2 == 0:
        print(i, ' Computer acts ')
        if i!=2:
            if me.points<=points*0.35:
                me.action(choice([1,1,2,3]))
            else:
                me.action(randint(1,3))
        else:
            me.action(randint(2,3))        
        print('You have ',me.points, ' points')
        print('Computer has ',computer.points, ' points')
    else:
        print(i, 'You act')
        if i!=1:
              if computer.points<=points*0.35:
                 computer.action(choice([1]*randint(2,5)+[2,3])) 
              else:
                computer.action(randint(1,3))
        else:
            computer.action(randint(2,3))
        print('Computer has ',computer.points, ' points')
        print('You have ',me.points, ' points')
    input()
            
if computer.points==0:
    print('You won')
else:
    print('Computer won')