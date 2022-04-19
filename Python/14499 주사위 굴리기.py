import sys
input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
# 주사위 굴리기
# 동서남북에 따라 값 위치 바꿔서 return
def move(n, dice):
    if n == 1:
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif n == 2:
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif n == 3:
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    elif n == 4:
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]

dice = [0 for _ in range(7)]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 명령 수행
for i in command:
    if 0 <= y+dy[i] < n and 0 <= x+dx[i] < m:
        x, y = x + dx[i], y + dy[i]
        dice = move(i, dice)
        if mat[y][x] == 0:
            mat[y][x] = dice[6]
        else:
            dice[6] = mat[y][x]
            mat[y][x] = 0
        print(dice[1])


