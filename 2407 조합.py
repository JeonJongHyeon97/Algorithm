import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = 1
for i in range(m):
    answer = answer * (n-i)
    answer = answer//(i+1)

print(answer)


