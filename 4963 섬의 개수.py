# -*- coding: utf-8 -*-
# BFS
import sys
input = sys.stdin.readline
from collections import deque

dy = [1, -1, 0, 0, 1, -1, 1, -1]
dx = [0, 0, 1, -1, -1, -1, 1, 1]

def bfs(y, x):
    s[y][x] = 0
    queue = deque()
    queue.append([y,x])
    while queue:
        yy, xx = queue.popleft()
        for k in range(8):
            new_y = yy + dy[k]
            new_x = xx + dx[k]
            if 0 <= new_x < w and 0 <= new_y < h and s[new_y][new_x] == 1:
                s[new_y][new_x] = 0
                queue.append([new_y, new_x])
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    s = []
    cnt = 0
    for i in range(h):
        s.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)