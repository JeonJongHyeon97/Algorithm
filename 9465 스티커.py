# Dynamic Programming
# 대각선으로 값을 선택하여 더했을때 최대인 경우 찾기
# 칸에 초기값을 넣고 대체하면서 전행
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
  dp = []
  n = int(input())
  for k in range(2):
    dp.append(list(map(int, input().split())))
  #두번째 칸은 대각선으로 바로 받는 경우 밖에 없으므로 미리 넣기
  dp[0][1] += dp[1][0]
  dp[1][1] += dp[0][0]

  for j in range(2, n):
    dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
    dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
  print(max(dp[0][n - 1], dp[1][n - 1]))