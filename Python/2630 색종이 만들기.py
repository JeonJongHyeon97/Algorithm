# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:38:39 2021

@author: user
"""
# 분할정복

# define devide and conquer funtion
def quad_tree(x: int, y: int, n: int):
    global matrix, blue, white
    color = matrix[y][x] # base color
    same_color = True # check point for same color
    
    for i in range(x, x+n):
        if not same_color:
            break
        # check included square's color
        for j in range(y, y+n):
            if matrix[j][i] != color: # if square contain 2 colors
                quad_tree(x, y, n//2) # second quadrant
                quad_tree(x + n//2, y, n//2) # first quadrant
                quad_tree(x, y + n//2, n//2) # third quadrant
                quad_tree(x + n//2, y + n//2, n//2) # fourth quadrant
                same_color = False # square contain 2 colors
                break
    
    if same_color: # all of included squares' color is same
        if matrix[y][x] == 1: # blue
            blue += 1
        else:
            white += 1 # white
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
quad_tree(0,0,N)
print(white)
print(blue)