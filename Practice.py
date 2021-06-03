import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

queue = deque([[0,0]])

while queue:
    a, b = queue.popleft()

    for i in range(4):
        aa = a + x[i]
        bb = b + y[i]
        if (aa,bb) != (0,0) and 0 <= aa < n and 0 <= bb < m and matrix[aa][bb] == 1:
            matrix[aa][bb] = matrix[a][b] + 1
            queue.append([aa, bb])

print(matrix[n-1][m-1])






