# DFS
# 인접한 배추들을 먼저 탐색하기
import sys
input = sys.stdin.readline
ans =[]
def DFS(x, y):
    global visited
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if (new_x, new_y) not in visited and 0<=new_x<m and 0<=new_y<n and field[new_y][new_x]==1:
            visited.append((new_x, new_y))
            DFS(new_x,new_y)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0 for i in range(m)] for j in range(n)]
    for __ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    count = 0
    visited = []
    for loc_x in range(m):
        for loc_y in range(n):
            if (loc_x, loc_y) not in visited and field[loc_y][loc_x] == 1:
                count +=1
                visited.append((loc_x, loc_y))
                DFS(loc_x, loc_y)
    ans.append(count)

for i in ans:
    print(i)


