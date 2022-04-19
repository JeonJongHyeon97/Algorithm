# 소수찾기
# 아리토스테네스의 체

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
num = [False for _ in range(n)]
num.extend([True for _ in range(n, m+1)])
for i in range(2, int(m**0.5)+1): # check up to square root m
    for j in range(2*i, m+1, i):
        num[j]=False
        
for i in range(2, len(num)):
    if num[i]:
        print(i)

