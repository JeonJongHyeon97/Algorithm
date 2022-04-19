# -*- coding: utf-8 -*-
"""
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
"""


n=int(input())
solve = []

def BackT(depth):
    if depth == n:
        print(" ".join(solve))
        return
    for i in range(1, n + 1):
        if str(i) not in solve:
            solve.append(str(i))
            BackT(depth + 1)
            solve.pop()

BackT(0)























