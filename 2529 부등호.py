import sys
input = sys.stdin.readline
n = int(input())
st = list(input().rstrip().split())

num = [i for i in range(10)]
answer=[]

def DFS(queue, visited):
    if len(queue) == n+1:
        answer.append(queue.copy())
        return
    idx = len(queue)-1
    if st[idx] == '<':
        for i in range(10):
            if visited[i] and queue[-1] < i:
                queue.append(i)
                visited[i] = False
                DFS(queue, visited)
                queue.pop()
                visited[i] = True
    elif st[idx] == '>':
        for i in range(10):
            if visited[i] and queue[-1] > i:
                queue.append(i)
                visited[i] = False
                DFS(queue, visited)
                queue.pop()
                visited[i] = True

for i in range(10):
    visit = [True for _ in range(10)]
    visit[i] = False
    DFS([i], visit)
answer.sort()
for i in answer[-1]:
    print(i, end="")
print()
for i in answer[0]:
    print(i, end="")
