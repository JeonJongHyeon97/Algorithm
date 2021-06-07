# 소수찾기
# 아리토스테네스의 체

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
num = [0 for _ in range(n)]
num.extend([i for i in range(n, m+1)])

for i in range(2, m+1): # 2qnxj
    for j in range(2*i, m+1, i):
        num[j]=0


num = list(set(num[2:]))
if 0 in num:
    num.remove(0)
for i in sorted(num):
    print(i)



