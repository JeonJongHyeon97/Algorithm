# -*- coding: utf-8 -*-

# 규칙 찾기

import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
cursor = 0
noAns=True
if n == 1:
    print(-1)
else:
    for i in range(n - 1, 0, -1):
        if s[i - 1] < s[i]: # find descending order from end to start
            cursor = i - 1  # cursor for swap
            break
    for i in range(n - 1, 0, -1):
        if s[cursor] < s[i]:    # find index(bigger than cursor) from end to start
            s[cursor], s[i] = s[i], s[cursor]   # swap
            s = s[:cursor + 1] + sorted(s[cursor + 1:]) # realignment from next index(cursor)
            print(*s)
            break
        if i == 1:  # last permutation
            print(-1)




