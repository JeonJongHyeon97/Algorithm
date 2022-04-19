import sys
import copy
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(m)]

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

tmp = copy.deepcopy(matrix)
flag = True
time = 0
cnt_one = 0
for row in matrix:
    for i in row:
        if i == 1:
            cnt_one += 1
while flag:
    queue = deque([[0, 0]])
    time += 1
    visited = [[True for i in range(n)] for j in range(m)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + moves[i][0]
            new_y = y + moves[i][1]
            if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y]:
                next_node = matrix[new_x][new_y]
                if next_node == 0:
                    queue.append([new_x, new_y])
                else:
                    tmp[new_x][new_y] = 0
                visited[new_x][new_y] = False
    matrix = copy.deepcopy(tmp)
    tmp_one = 0
    for row in matrix:
        for i in row:
            if i == 1:
                tmp_one += 1
    if tmp_one == 0:
        flag = False
    else:
        cnt_one = tmp_one
print(time)
print(cnt_one)
