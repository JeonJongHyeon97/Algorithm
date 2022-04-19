import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num= list(map(int, input().split()))
num.sort()
visited = [True for _ in range(n)]
answer = []

def DFS(queue, visited):
    global answer, m
    if len(queue) == m and queue:
        answer.append(tuple(queue))
        return
    for i in range(len(num)):
        if visited[i]:
            visited[i] = False
            queue.append(num[i])
            DFS(queue, visited)
            visited[i] = True
            queue.pop()
DFS([],visited)
answer = sorted(list(set(answer)))
for i in answer:
    print(*i)

