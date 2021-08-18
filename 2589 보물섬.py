from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    distance = 0
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visited[x][y] and matrix[x][y] != "W":
                visited[x][y] = False
                matrix[x][y] = matrix[a][b] + 1
                distance = max(distance, matrix[x][y])
                queue.append([x, y])
    return distance
result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != "W":
            visited = [[True for i in range(m)] for _ in range(n)]
            matrix[i][j] = 0
            visited[i][j] = False
            result = max(result, bfs(i, j))
print(result)