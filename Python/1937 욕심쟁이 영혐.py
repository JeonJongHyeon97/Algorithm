import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*100)

n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n and 0 <= ny < n) and s[x][y] < s[nx][ny]:
            dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, DFS(i, j))
print(answer)