import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
queue = deque([[a, 1]])
noAnswer = True
while queue:
    start, cnt = queue.popleft()
    addOne = start * 10 + 1
    double = start * 2
    if addOne == b or double == b:
        noAnswer = False
        print(cnt+1)
        break
    if addOne <= b:
        queue.append([addOne, cnt+1])
    if double <= b:
        queue.append([double, cnt+1])

if noAnswer:
    print(-1)