import numpy as np
import random
import matplotlib.pyplot as plt
import math
start = [2,4]
goal  = [9,9]
obstacles = [[2,6],[4,4],[6,2],[9,7],[5,7],[9,2],[3,9],[6,6]]
fig, ax = plt.subplots()
plt.xlim([0,10])
plt.ylim([0,10])
a_circle = plt.Circle((2,4),.2,color = 'red',label = 'start')
ax.add_artist(a_circle)
b_circle = plt.Circle((9, 9),.2,label = 'goal')
ax.add_artist(b_circle)
ax.legend()
i = 0
while i<len(obstacles):
    rect=obstacles[i]
    ax.plot(rect[0],rect[1],color = 'black',marker = 'D')
    i = i+1
plt.legend(["obstacles"])
def distanceCalculation(n0,n1x,n1y):
    dist = math.sqrt(((n1x-n0[0])**2)+((n1y-n0[1])**2))
    print('distance',dist)
    mindistance(dist,n1x,n1y,n0)
    return (dist) 
def mindistance(dist,n1x,n1y,n0):
    if dist > 3 :        
        print('distance checking')
        a = n1x-n0[0]
        b = n1y-n0[1]
        theta = math.atan2(b,a)
        n2x = round(n0[0]+1*math.cos(theta))
        n2y = round(n0[1]+1*math.sin(theta)) 
        obstacle_check(n2x,n2y)   
        return n2x,n2y
    else:
        pointsx.append(n1x)
        pointsy.append(n1y)        
def obstacle_check(n2x,n2y):    
    for j in obstacles:    
        if j == [n2x,n2y] or n2x > 10 or n2y > 10:
            print('line obstacle again encounter')
            break
    else:        
        obstaclesRemove(obsx,obsy)     
        eqn2(n2x,n2y,n0,obsx,obsy,m,yend)    
        for z in range(min(len(yend),len(obsy))):            
            if yend[z] < obsy[z]+0.5 and yend[z] > obsy[z]-0.5 or yend[z] > 2000 or yend[z] < -20000 :
                print('got line obstacle2')
                break
        else:
            pointsx.append(n2x)
            pointsy.append(n2y) 
            return pointsx,pointsy,n2x,n2y
        
def obstacleData(obstacles):    
    for k in obstacles:
        obsx.append(k[0])
        obsy.append(k[1]) 
    return (obsx,obsy)
def eqn(n1x,n1y,n0,obsx,obsy,m,yend):   
    obstacleData(obstacles)
    p = n1x-n0[0]
    q = n1y-n0[1]
    thet = math.atan2(q,p)
    m = math.tan(thet)
    for h in obsx:
        cy=round(m*(h-n0[0])+n0[1])
        yend.append(cy)          
    return (yend,p,q)
def obstaclesRemove(obsx,obsy):
    del obsx[0:8]
    del obsy[0:8]
    del yend[0:len(yend)+1]
    return (obsx,obsy)
def eqn2(n2x,n2y,n0,obsx,obsy,m,yend):   
    obstacleData(obstacles)
    p = n2x-n0[0]
    q = n2y-n0[1]
    thet = math.atan2(q,p)
    print('n0',n0)
    print('value',thet)
    m = math.tan(thet)    
    for d in obsx:
        cy=round(m*(d-n0[0])+n0[1])
        yend.append(cy)          
    print('elements2',yend)
    return (yend,p,q,n2x,n2y)
n0 = start
goalc = True
m=0
dist = 0
pointsx = [n0[0]]
pointsy = [n0[1]]

while goalc: 
    n1x = random.randint(0,10)
    n1y = random.randint(0,10)
    print('intial value',n0)
    print('generated',n1x,n1y)
    for j in obstacles:    
        if j == [n1x,n1y] or n1x > 10 or n1y > 10:
            print('got an obstacle')
            break
    else:
        obsx = []
        obsy = []
        yend=[]  
        eqn(n1x,n1y,n0,obsx,obsy,m,yend)
        for z in range(7):                    
            if yend[z] < obsy[z]+0.5 and yend[z] > obsy[z]-0.5 or yend[z] > 2000 or yend[z] < -20000  :
                print('got line obstacle')
                break
        else: 
            n2x = 0
            n2y = 0
            distanceCalculation(n0,n1x,n1y)
            e = len(pointsx)
            n0 = [pointsx[e-1],pointsy[e-1]]
    if n0 == goal :
        goalc = False
    else:
        goalc = True

plt.plot(pointsx,pointsy)
plt.title('RRT path Planning')
plt.show()              
                
                
    


