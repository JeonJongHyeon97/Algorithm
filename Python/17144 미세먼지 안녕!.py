import sys
import copy
input = sys.stdin.readline
R, C, T = map(int, input().split())
mat = []
air_locate = []
# 행렬 입력받기 및 공기청정기 위치 저장
for i in range(R):
    tmp = list(map(int, input().split()))
    mat.append(tmp)
    if tmp[0] == -1:
        air_locate.append(i)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def spread(matrix): # 미세먼지 확산 함수
    # 0으로 채워진 리스트 복사
    tmp = [[0 for _ in range(C)] for i in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c] not in [0, -1]: # 미세먼지가 있다면
                cnt=0   # 확산 횟수
                for i in range(4):
                    x = r + dx[i]
                    y = c + dy[i]
                    if 0<=x<R and 0<=y<C and matrix[x][y] != -1:
                        cnt+=1  # 확산 횟수 +1
                        tmp[x][y] += matrix[r][c]//5 # 미세먼지 확산
                tmp[r][c] += matrix[r][c] - (matrix[r][c]//5)*cnt   # 확산 후 남은 미세먼지량 저장
            elif matrix[r][c] == -1:    # 공기청정기가 있는경우
                tmp[r][c] = -1
    return tmp  # 확산후 행렬 리턴

def air(matrix): #   공기청정기 가동 함수
    # 윗공기 순환
    for i in range(air_locate[0]-1, 0, -1):
        matrix[i][0] = matrix[i-1][0]
    for i in range(0, C-1):
        matrix[0][i] = matrix[0][i+1]
    for i in range(0, air_locate[0]):
        matrix[i][-1] = matrix[i+1][-1]
    for i in range(C-1, 1, -1):
        matrix[air_locate[0]][i] = matrix[air_locate[0]][i-1]
    matrix[air_locate[0]][1] = 0
    # 아랫공기 순환
    for i in range(air_locate[1]+1, R-1):
        matrix[i][0] = matrix[i+1][0]
    for i in range(0, C-1):
        matrix[R-1][i] = matrix[R-1][i+1]
    for i in range(R-1, air_locate[1], -1):
        matrix[i][-1] = matrix[i-1][-1]
    for i in range(C-1, 1, -1):
        matrix[air_locate[1]][i] = matrix[air_locate[1]][i-1]
    matrix[air_locate[1]][1] = 0

second = 0
while(second!=T):
    second+=1
    mat = copy.deepcopy(spread(mat))
    air(mat)
answer=0
for i in mat:
    answer+=sum(i)
# 공기청정기가 -1이라서 +2해주기
print(answer+2)