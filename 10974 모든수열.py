# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:26:35 2021

@author: JongHyeon
"""


n=int(input())
solve = []

def BackT(depth):
    if depth == n:
        print(" ".join(solve))
        return
    for i in range(1, n + 1):
        # print("solve : ", solve)
        if str(i) not in solve:
            solve.append(str(i))
            BackT(depth + 1)
            solve.pop()

BackT(0)























