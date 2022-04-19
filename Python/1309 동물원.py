from collections import deque
import sys
N = int(sys.stdin.readline())
prepre = 3
pre = 7
for _ in range(N-1):
    prepre, pre= pre, (2*pre+prepre)%9901
print(prepre%9901)
