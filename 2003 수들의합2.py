# -*- coding: utf-8 -*-
"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
# 미리 합을 구하는 모든 경우의 수를 만들어 리스트화

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))

total=0
answer=0
for i in range(len(A)):
    total=A[i]
    if total == m:
        answer+=1
    elif total > m:
        continue
    else:
        for j in range(i+1, len(A)):
            total+=A[j]
            if total > m:
                break
            elif total == m:
                answer+=1
                break
            else:
                pass
print(answer)









