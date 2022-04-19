# -*- coding: utf-8 -*-
from collections import deque



board = []
snake = deque()
apple = []
move = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
k = int(input())

for _ in range(k):
    apple.append(list(map(int, input().split())))
L = int(input())
for _ in range(L):
    X, C = input().split()
    move.append([int(X), C])

snake.append([1,1])
stop = False
cnt = 0
c = 1
head = [1,1]
while not stop:
    board = [[' ' for i in range(n)] for j in range(n)]
    for ap in apple:
        board[ap[0]-1][ap[1]-1] = 7
    for sn in snake:
        board[sn[0]-1][sn[1]-1] = 8
    print("---------------------", cnt)
    for bd in board:
        print(*bd)
    head = [head[0]+dx[c], head[1]+dy[c]]
    # snake head is not on wall and it's body
    if 1 <= head[0] <= n and 1 <= head[1] <= n and head not in snake:
        snake.append(head)
        # not eat apple
        if head not in apple:
            snake.popleft()
            # print(snake)
        # eat apple
        else:    
            apple.remove(head)
    else:
        break
    cnt += 1
    # if change direction
    if len(move) > 0 and move[0][0] == cnt:
        X, C = move.popleft()
        if C == 'L':
            c = (c+3)%4
        else:
            c = (c+1)%4
    

    
print(cnt+1)
