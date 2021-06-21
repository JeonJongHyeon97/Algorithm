import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    print()
    print("i : ",i)
    print(sum[i] + a[i + 1])
    print(a[i + 1])
    print("append : ", max(sum[i] + a[i + 1], a[i + 1]))
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print("answer")
print(max(sum))


