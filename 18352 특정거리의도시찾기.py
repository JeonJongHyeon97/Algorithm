import sys
import math
from collections import defaultdict
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
answer = [math.inf for i in range(n+1)]
visited = [x]
matrix = defaultdict(list)
queue = []
for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)

queue.append([x, 1])
while(queue):
    start, w = queue.pop(0)
    if w <=k:
        for next in matrix[start]:
            if answer[next] >= w and next not in visited:
                answer[next] = w
                queue.append([next,w+1])
                visited.append(next)
if answer.count(k) == 0:
    print(-1)
else:
    for i in range(len(answer)):
        if answer[i] == k: print(i)
