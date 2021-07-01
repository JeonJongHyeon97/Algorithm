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
    print("--------j", j)
    total = 0
    nearest = 999999
    for i in house:
        print("house : ", i)
        for k in j:
            print(chicken[k])
            nearest = min(nearest, distance(i, chicken[k]))
            print("distance : ", distance(i, chicken[k]))
        total += nearest
    answer = min(answer, total)
print(answer)









