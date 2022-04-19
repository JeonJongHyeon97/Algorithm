# 유클리드 호제법으로 최대공약수(GCD) 구하기
import sys
from itertools import combinations
# find Greatest common dvisor
def GCD(big: int, small: int) -> int:
    tmp = 1
    while tmp:
        tmp = big % small  # if a % b == 0, b is GCD
        big, small = small, tmp
    return big

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    answer = 0
    for i in combinations(num,2):
        # answer += GCD(max(i[0],i[1]), min(i[0],i[1]))
        print(i[0],i[1])
    # print(answer)
