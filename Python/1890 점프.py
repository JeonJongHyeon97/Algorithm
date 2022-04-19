import sys
input = sys.stdin.readline

from collections import deque
n = int(input())

mat= [list(map(int, input().split())) for _ in range(n)]
answer = 0
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    jump = mat[x][y]
    if (x+jump == n-1 and y == n-1) or (x == n-1 and y+jump == n-1):
        answer+=1
        continue
    if 0 <= x+jump < n and 0 <= y< n:
        queue.append((x+jump, y))
    if 0 <= x < n and 0 <= y + jump < n:
        queue.append((x, y+jump))


print(answer)