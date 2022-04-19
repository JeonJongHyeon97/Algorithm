from collections import deque
import sys

input = sys.stdin.readline

matrix = [list(input().strip()) for _ in range(12)]
visited = [[False for i in range(6)] for _ in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
combo = 0
flag = True


def bfs():
    boom = False
    for i in range(12):
        for j in range(6):
            if visited[i][j] or matrix[i][j] == ".":  # 블럭이 없거나 visited
                visited[i][j] = True
                continue
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            pungs = []

            while queue:
                x, y = queue.popleft()
                pungs.append([x, y])
                now = matrix[x][y]
                if now != ".":
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if matrix[nx][ny] == now and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                cnt += 1
            if cnt >= 4:
                boom = True
                for pung in pungs:
                    matrix[pung[0]][pung[1]] = "."
    return boom


def down():
    for j in range(5, -1, -1):
        tmp = []
        for i in range(12):
            tmp.append(matrix[i][j])
        tmp = list(filter(lambda x: x != ".", tmp))
        new = ['.' for _ in range(12-len(tmp))]
        new.extend(tmp)
        # while len(tmp) != 12:
        #     tmp.insert(0, '.')
        for i in range(12):
            matrix[i][j] = new[i]


while flag:
    visited = [[False for i in range(6)] for _ in range(12)]
    combo += 1
    flag = bfs()
    # if flag:
    #     combo += 1
    down()

print(combo-1)
