import sys
input = sys.stdin.readline

n = int(input())

mat= [list(map(int, input().split())) for _ in range(n)]
answer=[0, 0, 0]

def DQ(x, y, m):
    global answer, mat
    cri = mat[x][y]
    cnt = 0
    for i in range(x, x+m):
        for j in range(y, y+m):
            if mat[i][j] != cri:
                for k in range(0, m, m//3):    # 0:3, 3:6. 6:9, 0:1, 1:2, 2:3
                    for l in range(0, m, m//3):

                        DQ(x+k, y+l, m//3)
                return
            else:
                cnt+=1
    if cnt == m*m:
        answer[cri] += 1


DQ(0, 0, n)
for i in [-1, 0, 1]:
    print(answer[i])
