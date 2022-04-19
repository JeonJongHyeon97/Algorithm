# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:00:54 2021

@author: JongHyeon
"""

n = int(input())
name =[]
k =1
for i in range(n):
    name.append(input())

tmp=[]
for i in range(1,len(name[0])+1):
    # print("i : ",i)
    for j in range(len(name)):
        # print("name : ", name[j])
        # print("last : ", name[j][-i:])
        if name[j][-i:] not in tmp:
            tmp.append( name[j][-i:])
        else:
            j-=1
            break
    if( j == len(name)-1):
        k=i
        break
print(k)