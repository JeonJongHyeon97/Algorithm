# -*- coding: utf-8 -*-
"""
정사각형으로 가려지는 점이란, 어떤 점이 그 정사각형의 한 변 위에 놓여져 있을 때, 정사각형으로 가려진다고 한다.

점이 N개가 주어진다. N개의 점 모두를 가릴 수 있는 정사각형을 구하는 프로그램을 작성하시오. 정사각형의 변은 x축과 y축에 평행해야 한다.
"""

n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=map(int, input().split())
    x.append(a)
    y.append(b)

gap = max(max(x)-min(x),max(y)-min(y))
answer=gap
for i in range(n):
    if x[i] not in [min(x),min(x)+gap]:
        if y[i] not in [min(y), min(y)+gap]:
            answer=-1
            break
        
    if y[i] not in [min(y), min(y)+gap]:
        if x[i] not in [min(x),min(x)+gap]:
            answer=-1
            break

        
print(answer)




