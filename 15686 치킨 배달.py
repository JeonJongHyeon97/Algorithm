import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
house=[]
chicken=[]
matrix = []
def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])



for i in range(n):
    tmp = list(map(int, input().split()))
    for j in list(filter(lambda x: tmp[x] == 1, range(len(tmp)))):
        house.append([i, j])
    for k in list(filter(lambda x: tmp[x] == 2, range(len(tmp)))):
        chicken.append([i, k])
tmp = 99999999
for j in combinations([k for k in range(len(chicken))], m):
    total = 0
    for i in house:
        total += distance(i, j)
    print(total)
    tmp = min(tmp, total)

print(tmp)









