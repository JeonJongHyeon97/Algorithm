import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(n + 1)]
result = sum(costs)

for i in range(0, n):

    byte = memory[i]
    cost = costs[i]

    for j in range(1, sum(costs) + 1):
        if j < cost: # cost 부족
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 앱을 끄는 경우와 이전의 경우 총합 메모리 비교
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])
        if dp[i][j] >= m:  # 충분한 메모리 확보한 경우
            result = min(result, j)

if m:
    print(result)
else:
    print(0)
