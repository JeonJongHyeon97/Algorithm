import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

num=sorted(num)
for i in range(m):
    a = num[0]
    b = num[1]
    num[0]=a+b
    num[1]=a+b
    num = sorted(num)

print(sum(num))





