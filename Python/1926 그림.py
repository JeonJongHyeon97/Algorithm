import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
visited = [[True for i in range(m)] for j in range(n)]
for _ in range(n):
    matrix.append(list(map(int, input().split())))
#
# for _ in matrix:
#     print(*_)
#
# for _ in visited:
#     print(*_)
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cnt = 0
max_space = [0]
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 1 and visited[x][y]:
            queue = [[x, y]]
            visited[x][y] = False
            cnt += 1
            space = 1
            while queue:
                a, b = queue.pop()
                for i in range(4):
                    new_a = a + d[i][0]
                    new_b = b + d[i][1]
                    print(new_a, new_b)
                    if 0 <= new_a < n and 0 <= new_b < m:
                        if matrix[new_a][new_b] == 1 and visited[new_a][new_b]:
                            queue.append([new_a, new_b])
                            space += 1
                        visited[new_a][new_b] = False
            max_space.append(space)
        visited[x][y] = False
print(cnt)
print(max(max_space))
