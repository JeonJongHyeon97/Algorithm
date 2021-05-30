# -*- coding: utf-8 -*-
"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
total=0
for i in range(0, n-1):
    total=a[i]
    if total == m:
        count+=1
    elif total < m:
        for j in range(i+1, n):
            if total+a[j] > m:
                break
            total += a[j]
            if total == m:
                count+=1
print(count)