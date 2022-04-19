import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
num=[]
for _ in range(n):
    c = int(input())
    if c <= k:  # only append coin smaller than k
        coin.append(c)
tmp = k
for c in coin[::-1]:    # from big coin to small coin
    if tmp == 0:
        break
    elif c<=tmp:
        num.append(tmp//c)  # append number of coin(maximum == tmp//c)
        tmp=tmp%c   # save balance
print(sum(num))

