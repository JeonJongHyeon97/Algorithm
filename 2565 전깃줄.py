import sys
input = sys.stdin.readline
n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
lines.sort(key=lambda x: x[0])
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))