# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:38:39 2021

@author: user
"""
# 분할정복

#쿼드 트리 함수 정의
def quad_tree(x, y, n):
    global matrix, blue, white # global 접근 제한자로 외부에 선언된 변수 가져오기
    color = matrix[y][x] # 첫 색깔과 나머지 색이 같아야함
    double_break = False # for문 탈출용 double_break
    
    for i in range(x, x+n):
        if double_break:
            break
            
        for j in range(y, y+n):
            if matrix[j][i] != color: # 정사각형이 같은 색으로 이루어져있지 않다면, 4조각으로 나누기
                quad_tree(x, y, n//2) # 2사분면
                quad_tree(x + n//2, y, n//2) # 1사분면
                quad_tree(x, y + n//2, n//2) # 3사분면
                quad_tree(x + n//2, y + n//2, n//2) # 4사분면
                double_break = True # 탈출!
                break
    
    if not double_break:
        if matrix[y][x] == 1: # 파란색이라면
            blue += 1
        else:
            white += 1 # 흰색이라면


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

quad_tree(0,0,N)
print(white)
print(blue)