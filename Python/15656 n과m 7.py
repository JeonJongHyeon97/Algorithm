import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int,input().split())))

def DFS(answer:list):
    global n, m, num
    if len(answer) == m:
        print(*answer)
        return
    for i in num:
        answer.append(i)
        DFS(answer)
        answer.pop()
DFS([])