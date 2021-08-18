import sys
input = sys.stdin.readline
n = int(input())
matrix = []
maxdegree = 0
for _ in range(n):
    tmp = list(map(int,input().split()))
    maxdegree = max(maxdegree, max(tmp))
    matrix.append(tmp)

move = [(1,0), (0,1), (-1,0), (0,-1)]
def DFS(a, b, k):
    for j in range(4):
        x = a + move[j][0]
        y = b + move[j][1]
        if 0 <= x < n and 0 <= y < n and matrix[x][y] > k and (x,y) not in visited :
            visited.append((x, y))
            DFS(x,y, k)


answer = 0
check = 0
for i in range(maxdegree-1, -1, -1):
    visited = []
    cnt = 0
    for x in range(n):
        for y in range(n):
            if matrix[x][y] > i and (x,y) not in visited:
                cnt += 1
                visited.append((x, y))
                DFS(x,y,i)
    # print(cnt)
    # print(visited)
    if cnt < answer:
        check += 1
        if check == 2:
            break

    answer = max(answer, cnt)

print(answer)


