#Dynamic programming
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = num.copy()
print("num : ", num)
for i in range(n):
    print("-------------", i)
    for j in range(i):
        print("j : ", j)
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])
            print(dp)
print(max(dp))