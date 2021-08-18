# BFS
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, -2, 2, 1, -1]
for t in range(int(input())):
    l = int(input())
    visited = [[True for _ in range(l)]for __ in range(l)]
    matrix = [[0 for _ in range(l)]for __ in range(l)]
    queue = deque()
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    queue.append([s_x, s_y])
    if (s_x, s_y) == (e_x, e_y):
        print(0)
        continue
    move = 0
    repeat = True
    while repeat:
        x, y = queue.popleft()
        visited[x][y] = False
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < l and 0 <= new_y <l and visited[new_x][new_y]:
                matrix[new_x][new_y] = matrix[x][y] +1
                if new_x == e_x and new_y == e_y:
                    repeat = False
                    break
                queue.append([new_x, new_y])
                visited[new_x][new_y] = False
    print(matrix[e_x][e_y])






