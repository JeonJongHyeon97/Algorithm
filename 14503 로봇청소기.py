import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
dd = [-1,0,1,0,-1,0,1,0]
matrix = [list(map(int, input().split())) for _ in range(n)]
repeat = True
back = True
cnt = 0
mid_stop= False
while repeat:
    back = True
    mid_stop=False
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        cnt += 1
    matrix[r][c] = 2

    for i in range(1, 5):
        d = (d + 3) % 4
        rr, cc = r, c

        rr = r + dd[d-1]
        cc = c + dd[3-d+i]
        if i == 2:
            if 0 <= rr < n and 0 <= cc < m and matrix[rr][cc] == 1:
                back = False
            br, bc = rr, cc
        if 0 <= rr < n and 0 <= cc < m and matrix[rr][cc] == 0:
            r, c = rr, cc
            mid_stop=True
            break
    if mid_stop:
        continue
    if back:
        r, c = br, bc
        continue
    else:
        break
print(cnt)
