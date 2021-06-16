# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = defaultdict(list)
    for __ in range(int(input())):
        cloth, body = input().rstrip().split()
        clothes[body].append(cloth)
    if len(clothes) == 0:
        print(0)
        continue
    answer=1
    for key in clothes.keys():
        answer *= (len(clothes[key])+1)
    print(answer-1)
    