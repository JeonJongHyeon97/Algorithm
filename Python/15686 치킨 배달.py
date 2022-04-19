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

answer = 99999999
for j in combinations(range(len(chicken)), m):
    total = 0
    for i in house:
        nearest = 999999
        for k in j:
            nearest = min(nearest, distance(i, chicken[k]))
        total += nearest
    answer = min(answer, total)
print(answer)









