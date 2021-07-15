import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def DFS(queue, visited):
    global cnt, num
    last = queue[-1]
    if not visited[num[last]]:
        num[last] = 0
        cnt += 1
        return
    queue.append(num[last])
    visited[num[last]] = False
    num[last] = 0
    DFS(queue, visited)


for _ in range(int(input())):
    n = int(input())
    num = [0]+list(map(int, input().split()))
    cnt = 0
    visited=[True for _ in range(n+1)]
    for i in range(1, (n+1)):
        if num[i] != 0:
            queue=[i]
            visited[i] = False
            DFS(queue, visited)
    print(cnt)

