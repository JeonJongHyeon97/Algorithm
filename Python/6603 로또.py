# -*- coding: utf-8 -*-
# 조합 이용해서 그냥 해결


from itertools import combinations
import sys
input = sys.stdin.readline
while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    for i in combinations(num[1:], 6):
        print(*i)
    print()
