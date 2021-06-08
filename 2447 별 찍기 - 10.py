# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:41:30 2021

@author: user
"""
# 분할정복
# 미리 *로 채워진 리스트를 만들고, 분할 정복하며 지우기

n = int(input())
matrix = [["*"]*n for _ in range(n)] # matrix(full of *)

# function for ddvide and conquer and remove *(center of square)
def star(x: int, y: int, n: int):
    for i in range(n//3,n//3*2):
        for j in range(n//3, n//3*2):
            matrix[x+i][y+j]=" "     # remove * (center of square)
    if n > 3:   # n < 3 -> can't divide into small square
        for i in range(1,4):
            for j in range(1,4):    # tripartitioning and conquer
                if i != 2 or j != 2:    # center of square -> pass
                    star(x+(i-1)*(n//3),y+(j-1)*(n//3),n//3)

star(0, 0, n)

for i in matrix:
    print("".join(i))

