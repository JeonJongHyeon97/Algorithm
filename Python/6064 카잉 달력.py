import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    list1 = set([x for x in range(x, m*n+1, m)])
    list2 = set([y for y in range(y, m*n+1, n)])
    intersect = list1.intersection(list2)
    print(list1)
    print(list2)
    if len(intersect)==0:
        print(-1)
    else:
        print(sorted(list(intersect))[0])