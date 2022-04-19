import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue=deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])


while queue:
    x, y = queue.popleft()
    for i in range(4):
        move_x = x + dx[i]
        move_y = y + dy[i]
        if 0<= move_x<n and 0<=move_y<m and tomato[move_x][move_y] == 0:
            tomato[move_x][move_y] = tomato[x][y] + 1
            queue.append([move_x,move_y])

answer = 0
complete = True
for i in tomato:
    answer = max(answer, max(i))
    if 0 in i:
        complete = False
if not complete:
    print(-1)
else:
    print(answer-1)













