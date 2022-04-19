# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:41:43 2021

@author: user
"""
# 돌이 밖으로 나가는 경우만 생각하여 그냥 코딩...
#

k, s, n = map(str, input().split())

abc = ["A","B", "C", "D", "E", "F", "G", "H"]
king=[abc.index(k[0])+1,int(k[1])]
stone=[abc.index(s[0])+1,int(s[1])]


def move(direction):
    if (direction == "R" and king[0]!=8):
        king[0]+=1
        if (king==stone and stone[0]!=8):
            stone[0]+=1
        elif (king==stone and stone[0]==8):
            king[0]-=1
    if (direction == "L" and king[0]!=1):
        king[0]-=1
        if (king==stone and stone[0]!=1):
            stone[0]-=1
        elif (king==stone and stone[0]==1):
            king[0]+=1
    if (direction == "B" and king[1]!=1):
        king[1]-=1
        if (king==stone and stone[1]!=1):
            stone[1]-=1
        elif (king==stone and stone[1]==1):
            king[1]+=1            
    if (direction == "T" and king[1]!=8):
        king[1]+=1
        if (king==stone and stone[1]!=8):
            stone[1]+=1
        elif (king==stone and stone[1]==8):
            king[1]-=1
    if (direction == "RT" and king[0] != 8 and king[1] != 8):
        king[0] += 1
        king[1] += 1
        if (king==stone and stone[0]!=8 and stone[1]!=8):
            stone[0] += 1
            stone[1] += 1
        elif (king==stone and (stone[0]==8 or stone[1]==8)):
            king[0] -=1
            king[1] -=1
    if (direction == "LT" and king[0] != 1 and king[1] != 8):
        king[0] -= 1
        king[1] += 1
        if (king==stone and stone[0]!=1 and stone[1]!=8):
            stone[0] -= 1
            stone[1] += 1
        elif (king==stone and (stone[0]==1 or stone[1]==8)):
            king[0] +=1
            king[1] -=1            
    if (direction == "RB" and king[0] != 8 and king[1] != 1):
        king[0] += 1
        king[1] -= 1
        if (king==stone and stone[0]!=8 and stone[1]!=1):
            stone[0] += 1
            stone[1] -= 1
        elif (king==stone and (stone[0]==8 or stone[1]==1)):
            king[0] -=1
            king[1] +=1
    if (direction == "LB" and king[0] != 1 and king[1] != 1):
        king[0] -= 1
        king[1] -= 1
        if (king==stone and stone[0]!=1 and stone[1]!=1):
            stone[0] -= 1
            stone[1] -= 1
        elif (king==stone and(stone[0]==1 or stone[1]==1)):
            king[0] +=1
            king[1] +=1


for i in range(int(n)):
    move(input())                             
    print(abc[int(king[0])-1]+str(king[1]))
    print(abc[int(stone[0])-1]+str(stone[1]))
print(abc[int(king[0])-1]+str(king[1]))
print(abc[int(stone[0])-1]+str(stone[1]))























