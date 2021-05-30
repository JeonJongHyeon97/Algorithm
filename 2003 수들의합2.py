# -*- coding: utf-8 -*-
"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
sum_A = [0] * (n + 1)
for i in range(1, n + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
answer = 0
for i in range(n):
    for j in range(i+1, n+1):
        if sum_A[j] < m: 
            pass
        elif sum_A[j] - sum_A[i] > m:
            break
        elif sum_A[j] - sum_A[i] == m:
            answer += 1
            break
            
print(answer)    
