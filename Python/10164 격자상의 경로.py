import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[0][i] = 1

# 경우의 수 매트릭스 만들기
for x in range(1, n):
    tmp = 1  # 누적합
    for y in range(m):
        matrix[x][y] = tmp
        if y != m - 1:
            tmp += matrix[x - 1][y + 1]

# for i in matrix:
#     print(*i)

if (k != 0):
    if k % m == 0:
        x = k//m
        y = m
    else:
        x = k // m + 1
        y = k % m
    answer = matrix[x - 1][y - 1] # 체크포인트 까지 경로의 수
    answer = answer*matrix[n - x][m - y] # 체크포인트 부터 끝까지 경로의 수
    print(answer)

else:
    print(matrix[n - 1][m - 1])
