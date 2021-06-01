# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:03:34 2021

@author: user
"""

n, m = map(int, input().split())
num = list(map(int, input().split()))
num=sorted(num)
solve = []

def BackT(depth):
    if depth == m:
        print(" ".join(solve))
        return
    for i in range(0, n):
        if str(num[i]) not in solve:
            solve.append(str(num[i]))
            BackT(depth + 1)
            solve.pop()

BackT(0)