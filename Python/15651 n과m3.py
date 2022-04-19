# -*- coding: utf-8 -*-
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""

n, m = map(int, input().split())
solve = []

def BackT(start, depth):
    if depth == m:
        print(" ".join(solve))
        return
    for i in range(start, n + 1):
        # print("solve : ", solve)
        if str(i) not in solve:
            solve.append(str(i))
            BackT(i, depth + 1)
            solve.pop()

BackT(1, 0)
