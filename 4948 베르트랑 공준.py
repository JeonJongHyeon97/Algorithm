import sys
input = sys.stdin.readline
num = [True for _ in range((123457*2)+1)]
for i in range(2, int((123457*2)**0.5)+1): # check up to square root m
    for j in range(2*i, (123457*2)+1, i):
        num[j]=False
# num.extend([True for _ in range(n, m+1)])
while True:
    n = int(input())
    if n == 0:
        break
    mini = num[n+1:(2*n)+1]
    print(len(list(filter(lambda x: x == True, mini))))

