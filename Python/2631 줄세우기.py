import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:   # 이어지는 숫자인지 (수열에 포함될 수 있는지)
            dp[i] = dp[j]
    dp[i] += 1  # 수열 길이 + 1

print(n-max(dp))





