import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
dp = [99999] * (k + 1)
dp[0] = 0
for _ in range(n):
   coins.append(int(input()))

for coin in sorted(coins):
    for j in range(coin, k + 1):
        dp[j] = min(dp[j - coin] + 1, dp[j]) # 이전동전들로 값맞추기 vs 새로운동전 사용하기

if dp[-1] == 99:
    print(-1)
else:
    print(dp[-1])