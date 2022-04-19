import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = [9999999 for _ in range(n+1)]
print(answer)
def DFS(tmp,queue):

    global answer
    if len(queue) == n:
        w = matrix[queue[-1]][0]
        if w != 0:
            tmp.append(tmp[-1]+w)
            print()
            print(tmp)
            print(queue)
            if tmp[-1] < answer[-1]:
                answer = tmp.copy()
        return
    for i in range(n):
        w = matrix[queue[-1]][i]
        if w != 0 and i not in queue and tmp[-1]+w <= answer[-1]:
            queue.append(i)
            tmp.append(tmp[-1]+w)
            DFS(tmp,queue)
            queue.pop()
            tmp.pop()


DFS([0],[0])
print(answer[-1])