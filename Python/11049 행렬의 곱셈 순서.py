import sys

input = sys.stdin.readline

n = int(input())
matrix = [] # 곱셈 횟수
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]

for diagonal in range(1, n):
    for row in range(0, n - diagonal):
        if diagonal == 1:
            dp[row][row + diagonal] = matrix[row][0] * matrix[row][1] * matrix[row + diagonal][1]
        else:
            dp[row][row + diagonal] = 999999999999
            for first_group in range(row, row + diagonal):
                dp[row][row + diagonal] = min(dp[row][row + diagonal], dp[row][first_group] + dp[first_group + 1][row + diagonal] + matrix[row][0] * matrix[first_group][1] * matrix[row + diagonal][1])

# print(dp[0][n - 1])

for i in dp:
    print(*i)