#dfs 유형
#노드간의 연결을 딕셔너리로 그래프 만든 후 해결
n = int(input())
graph={}
for i in range(n):
    graph[i+1] = set()
line = int(input())
for j in range(line):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(start, graph):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph)
visited = []
dfs(1, graph)
print(len(visited)-1)

