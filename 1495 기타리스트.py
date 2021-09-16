import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
result = [False for _ in range(m + 1)] # 조정된 볼륨
result[s] = True
flag = True
for vol in volumes:
    tmp = [False for _ in range(m + 1)]
    for i in range(len(result)):
        if result[i]:
            if 0 <= i - vol:
                tmp[i - vol] = True
            if i + vol <= m:
                tmp[i + vol] = True
    if True not in tmp:
        print(-1)
        flag = False
        break
    else:
        result = tmp
if flag:
    print(m-list(reversed(result)).index(True))