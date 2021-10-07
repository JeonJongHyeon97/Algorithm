import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 1: 가로, 2: 대각선, 3: 세로
queue = deque([[1, 0, 1]])
moves = {1: [[1, 0, 1], [2, 1, 1]], 3: [[3, 1, 0], [2, 1, 1]], 2: [[1, 0, 1], [3, 1, 0], [2, 1, 1]]}
dp = [[0 for _ in range(n)] for i in range(n)]
while queue:
    direction, x, y = queue.popleft()
    for move in moves[direction]:
        next_x = x + move[1]
        next_y = y + move[2]
        next_direction = move[0]
        if 0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] != 1:
            if next_direction == 2 and (matrix[next_x - 1][next_y] == 1 or matrix[next_x][next_y - 1] == 1):
                continue
            if (next_direction == 1 and next_y == n - 1 and next_x != n - 1) or (
                    next_direction == 3 and next_x == n - 1 and next_y != n - 1):
                continue
            dp[next_x][next_y] += 1
            queue.append([next_direction, next_x, next_y])

print(dp[n - 1][n - 1])

