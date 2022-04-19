import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
dp=[1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))

