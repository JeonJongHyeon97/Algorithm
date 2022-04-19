# -*- coding: utf-8 -*-
# 상하좌우 움직이는 리스트 dx, dy 미리만들기
# 상하좌우 탐색할 시작점을 queue에 넣고 dfs 느낌
n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]  # 상하좌우에 해당하는 좌표값 +/-
dy = [0, 0, -1, 1]

for i in range(n):
    s.append(list(input()))
    
queue = [[0, 0]]    # 첫 시작점 (0,0)
s[0][0] = 1

while queue:    # queue에 있는 시작점을 모두 처리할 때까지 반복
    a, b = queue[0][0], queue[0][1] # 시작점으로 설정
    del queue[0]    # 처리한 시작점은 제거
    for i in range(4):  # 상하좌우에 대해서 탐색
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":    # 좌표평면 위의 점이고 1이라면
            queue.append([x, y])    # 새로운 탐색 시작점이므로 queue에 추가
            s[x][y] = s[a][b] + 1   # 이전의 출발점에서 +1한 값을 대입
            
print(s[n - 1][m - 1])

