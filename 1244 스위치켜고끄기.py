# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:18:02 2021

@author: JongHyeon
"""

n = int(input())
switch = list(map(int, input().split()))
# n=8
# switch = [0, 1, 1, 1, 0, 1, 0, 1]
sex=[]
card=[]
num = int(input())
for i in range(num):
    a,b=map(int,input().split())
    sex.append(a)
    card.append(b)
    
for i in range(len(card)):
    # print(sex[i])
    # print(card[i])
    if sex[i]==1:
        for j in range(1,(len(switch)//(card[i]))+1):
            if(switch[(card[i])*j-1]==0): 
                switch[(card[i])*j-1]=1 
            else: 
                switch[(card[i])*j-1]= 0
    else:
        count=0
        do=-1
        # print("min : ", min(card[i]-1,len(switch)-card[i]))
        while(count<=min(card[i]-1,len(switch)-card[i])):
            # print(card[i]-1-(count))
            # print(card[i]-1+(count))
            if (switch[card[i]-1-(count)] == switch[card[i]-1+(count)]):
                count+=1
                do+=1
            else:
                break
        # print("do : ",do)
        for j in range(card[i]-1-do, card[i]+do):
            if(switch[j]==0): 
                switch[j]=1 
            else: 
                switch[j]= 0
    # print(switch)
answer=" ".join(list(map(str,switch)))
# answer="1 "*88+"1"
for i in range(0, (len(answer)//40)+1):
    print(answer[i*40:(i+1)*40])
    
    










