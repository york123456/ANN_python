# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:15:44 2022

@author: b4100
"""

'''
單層感知機
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

l=1e-1

w24=1
w34=1
b=1

k=0
while(1):
    k+=1
    
    E=0
    for i in range(4):
        x2=train[i][0]
        x3=train[i][1]
        ytarget=train[i][2]
        
        
        y2=x2
        y3=x3
        x4=y2*w24+y3*w34+b
        youtput=f(x4)
        
        w24=w24-l*y2*df(x4)*(youtput-ytarget)
        w34=w34-l*y3*df(x4)*(youtput-ytarget)
        b=b-l*df(x4)*(youtput-ytarget)
        
        E+=0.5*pow((youtput-ytarget),2)
    if E<1e-2:
        break
    if k>100000:
        print('\ntime out\n')
        break
    
print("count=",k,"      Error=",E,"\n")
print('x y f youtput             youtput-f')
for i in range(4):
    x2=train[i][0]
    x3=train[i][1]
    ytarget=train[i][2]
    y2=x2
    y3=x3
    x4=y2*w24+y3*w34+b
    youtput=f(x4) 
    print(x2,x3,ytarget,youtput,youtput-ytarget)
