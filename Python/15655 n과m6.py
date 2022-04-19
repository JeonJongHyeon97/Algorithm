from itertools import combinations
n, m = map(int, input().split())
num = list(map(int,input().split()))
output=[]
for i in combinations(num,m):
    output.append(sorted(list(i)))

for i in sorted(output):
    print(*i)




