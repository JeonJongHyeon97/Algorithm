import sys
input = sys.stdin.readline
m = 1000000
num=[True for _ in range(m + 1)]
for i in range(2, int(m ** 0.5) + 1):  # check up to square root m
    for j in range(2 * i, m + 1, i):
        num[j] = False
while True:
    n = int(input())
    if n ==0:
        break
    for i in range(2, len(num)):
        if num[i] & num[n-i]:
            print("{} = {} + {}".format(n,i,n-i))
            break
