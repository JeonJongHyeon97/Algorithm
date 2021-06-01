# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:41:30 2021

@author: user
"""
# 분할정복
# 미리 *로 채워진 리스트를 만들고, 분할 정복하며 지우기

n = int(input())
graph = [["*"]*n for _ in range(n)] # 미리 *로 채워진 행렬 선언

def star(x, y,n):
    for i in range(n//3,n//3*2):
        for j in range(n//3, n//3*2):
            graph[x+i][y+j]=" "     # 가운데 부분만 *을 공백으로 대체
    if n > 3:   # n이 3보다 작으면 더이상 나눌수 없음
        for i in range(1,4):
            for j in range(1,4):    # 3분할 정복
                if i != 2 or j != 2:
                    star(x+(i-1)*(n//3),y+(j-1)*(n//3),n//3)

star(0, 0, n)

for i in graph:
    print("".join(i))

