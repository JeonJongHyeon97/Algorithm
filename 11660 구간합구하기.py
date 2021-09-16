import sys
input=sys.stdin.readline
N, M = map(int, input().split())
matrix = [[0 for _ in range(N+1)]]
for k in range(N):
    row=[0]
    tmp = 0
    num =  list(map(int, input().split()))
    for i in range(len(num)):
        tmp += num[i]
        row.append(tmp+ matrix[-1][i+1])
    matrix.append(row)
print(matrix)
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2]-matrix[x1-1][y2]-matrix[x2][y1-1]+matrix[x1-1][y1-1])

