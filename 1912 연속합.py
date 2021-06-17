import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = []
for i in range(len(num)):
    if num[i] < 0:
      dp.append(sum(num[:i]))
      dp.append(num[i])
start = 0
end = 0
for i in range(len(dp)-1):
    if dp[i] + dp[i+1] >= 0:
        end = i+1
    elif dp[i] + dp[i+1] < 0:


