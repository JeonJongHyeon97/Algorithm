# -*- coding: utf-8 -*-



# Dynamic programming
# 주어진 문제를 작은 부분 문제로 생각해서 풀기
# dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1 점화식을 이용


n = int(input())

dpList = [0,0,1,1]

for i in range(4, n+1):
    dpList.append(dpList[i-1]+1)
    
    if i%2 == 0:
        dpList[i]=min(dpList[i],dpList[i//2]+1)
        
    if i%3 == 0:
        dpList[i]=min(dpList[i],dpList[i//3]+1)

print(dpList[n])

