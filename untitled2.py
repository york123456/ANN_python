# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:50:52 2022

@author: b4100
"""

'''
雙層三個感知機
'''

import math

def f(x):
    return 1/(1+math.exp(-x))

def df(x):
    return f(x)*(1-f(x))


#train=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]  #AND
#print("AND")


#train=[[0,0,0],[0,1,1],[1,0,1],[1,1,1]] #OR
#print("OR")

#train=[[0,0,1],[0,1,1],[1,0,1],[1,1,0]]  #NAND
#print("NAND")

train=[[0,0,1],[0,1,0],[1,0,0],[1,1,1]]  #XOR
print("XOR")

l=1e-2

w24=0.5
w34=0.1
w02=0.5
w03=0.5
w13=0.1
w12=0.5
b2=0.1
b3=0.5
b4=0.5

k=0
while(1):
    k+=1
    
    E=0
    for i in range(4):
        x0=train[i][0]
        x1=train[i][1]
        ytarget=train[i][2]
        
        
        y0=x0
        y1=x1
        
        x2=y0*w02+y1*w12+b2
        x3=y0*w03+y1*w13+b3
        y2=f(x2)
        y3=f(x3)
        
        x4=y2*w24+y3*w34+b4
        youtput=f(x4)
        
        
        
        w24=w24-l*y2*df(x4)*(youtput-ytarget)
        w34=w34-l*y3*df(x4)*(youtput-ytarget)
        b4=b4-l*df(x4)*(youtput-ytarget)
        
        
        
        w02=w02-l*y0*df(x2)*w24*df(x4)*(youtput-ytarget)
        w03=w03-l*y0*df(x3)*w34*df(x4)*(youtput-ytarget)
        
        w12=w12-l*y1*df(x2)*w24*df(x4)*(youtput-ytarget)
        w13=w02-l*y1*df(x3)*w34*df(x4)*(youtput-ytarget)
        
        b2=b2-l*df(x2)*w24*df(x4)*(youtput-ytarget)
        b3=b3-l*df(x3)*w34*df(x4)*(youtput-ytarget)
        
        
        E+=0.5*pow((youtput-ytarget),2)
    if E<1e-2:
        break
    if k>1000000:
        print('\ntime out\n')
        break
    
print("count=",k,"      Error=",E,"\n")
print('x y f youtput             youtput-f')
for i in range(4):
    x0=train[i][0]
    x1=train[i][1]
    ytarget=train[i][2]
    
    y0=x0
    y1=x1
    
    x2=y0*w02+y1*w12+b2
    x3=y0*w03+y1*w13+b3
    y2=f(x2)
    y3=f(x3)
    
    x4=y2*w24+y3*w34+b4
    youtput=f(x4)
    
    print(x0,x1,ytarget,youtput,youtput-ytarget)
