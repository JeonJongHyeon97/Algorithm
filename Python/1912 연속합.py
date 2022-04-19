import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
Sum = [a[0]]
for i in range(len(a) - 1):
    print()
    print("i : ",i)
    print(Sum[i] + a[i + 1])
    print(a[i + 1])
    print("append : ", max(Sum[i] + a[i + 1], a[i + 1]))
    Sum.append(max(Sum[i] + a[i + 1], a[i + 1]))
print("answer")
print(max(Sum))


