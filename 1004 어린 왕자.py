# -*- coding: utf-8 -*-
"""
시작점과 끝점이 내부에 위치하는 원의 갯수를 각각 구한후,
공통으로 내부에 있는 원은 제외한다.
"""

t = int(input())

for __ in range(t):
    s_x, s_y, e_x, e_y = map(int, input().split())
    n = int(input())
    galaxy = []
    relation_s = [0]*n
    relation_e = [0]*n
    start=0
    end=0
    for _ in range(n):
        galaxy.append(list(map(int, input().split())))
        
    for i in range(n):
        gal=galaxy[i]
        if ((s_x-gal[0])**2+(s_y-gal[1])**2) < gal[2]**2:   # 시작점이 내부에 있는 원 구하기
            relation_s[i]=1
        if ((e_x-gal[0])**2+(e_y-gal[1])**2) < gal[2]**2:   # 끝점이 내부에 있는 원 구하기
            relation_e[i]=1
    answer=0
    for i in range(len(relation_s)):
        if relation_s[i] != relation_e[i]:  # 두점 모두 내부에 있거나, 있지 않은 경우는 제외
            answer+=1
    print(answer)
