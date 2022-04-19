
"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""
# DFS나 BFS이용


graph = [] 
n = int(input())
answer = [] 
dx = [0,0,1,-1] #동서남북 인접한 곳의 좌표를 구하기 위함 
dy = [1,-1,0,0]
cnt = 0 
for _ in range(n):
    x = list(map(int,input()))
    graph.append(x)
    
def dfs(x,y):
    global cnt
    graph[x][y] = 0 # 처음 시작(탐색)한 곳은 0으로 바꿔줌
    cnt += 1 #집을 하나씩 탐색할때마다 +1 해준다
    for k in range(4): #동서남북 인접한 네 방향에 대해서 탐색
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] ==1: #인접한 곳의 좌표가 범위안이고 = 1
            graph[nx][ny] = 0 # 방문했던 곳은 0으로 다시 바꿔줌 
            dfs(nx,ny) # 탐색에 성공한 곳에서 다시 시작
    return cnt # 단지에 포함되는 집의 갯수

for i in range(n): # 그래프를 한칸씩 탐색(dgs함수 대입)
    for j in range(n):
        if graph[i][j] == 1: # 1이면 거기서 부터 dfs 함수 실행
            cnt = 0 # 단지에 포함되는 집의 갯수 초기화
            answer.append(dfs(i,j))
            
print(len(answer)) # 전체 단지 수
answer.sort()
for i in answer:
    print(i)