import sys

input = sys.stdin.readline

n = int(input())
cases = [0 for _ in range(41)]
cases[0] = 1
cases[1] = 1
cases[2] = 2
cases[3] = 3
tmp = 4
while tmp < 41:
    cases[tmp] = cases[tmp - 1] + cases[tmp - 2]
    tmp += 1
answer = 1
before_vip = 0
m = int(input())
for _ in range(m):
    vip = int(input())
    answer *= (cases[vip - 1 - before_vip])
    before_vip = vip
answer *= (cases[n - before_vip])
print(answer)
