# BruteForce
# 같은 값이 들어올수있으니 index로 조합 구하기

import sys
input = sys.stdin.readline

n =  int(input())
num = list(map(int, input().split()))
combi = []
tmp = []
stack = []
answer=0
for i in range(n):
    tmp.append(i)
    stack.append(tmp.copy())
    tmp.pop()
while stack:
    queue=stack.pop()
    if len(queue) == n:
        tmp = [abs(num[queue[i - 1]] - num[queue[i]]) for i in range(1, n)]
        answer = max(answer, sum(tmp))
    else:
        for i in range(n):
            if i not in queue:
                queue.append(i)
                stack.append(queue.copy())
                queue.pop()

print(answer)