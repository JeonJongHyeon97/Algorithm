# -*- coding: utf-8 -*-

n = int(input())

dpList=[1,1]

if n == 2 or n == 1:
    print(1)
else:
    for i in range(2,n):
        dpList.append(dpList[i-1]+dpList[i-2])
    print(dpList[-1])
