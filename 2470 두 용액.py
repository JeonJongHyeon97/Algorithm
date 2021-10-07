import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
start, end = 0, n - 1
answerStart, answerEnd = 0, n - 1
mix = abs(num[start] + num[end])
while start < end:
    tmp = num[start] + num[end]
    absTmp = abs(tmp)
    if absTmp < mix:
        answerStart, answerEnd = start, end
        mix = absTmp
        if tmp == 0:
            break
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(num[answerStart], num[answerEnd])
