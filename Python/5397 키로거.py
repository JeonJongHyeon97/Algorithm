# -*- coding: utf-8 -*-
# Using deque (Stack)
# left + cursor + right

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    left = deque([])
    right = deque([])
    pw = list(input().rstrip())
    for word in pw:
        if word == '<' and left:
            right.appendleft(left.pop())
        elif word == '>' and right:
            left.append(right.popleft())
        elif word == '-' and left:
            left.pop()
        elif word not in ['<', '>', '-']:
            left.append(word)
    print("".join(left)+"".join(right))
