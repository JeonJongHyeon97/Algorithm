# 유클리드 호제법으로 최대공약수(GCD) 구하기
import sys

input = sys.stdin.readline
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())


# find Greatest common dvisor
def GCD(big: int, small: int) -> int:
    tmp = 1
    while tmp:
        tmp = big % small  # if a % b == 0, b is GCD
        big, small = small, tmp
    return big


gcd = GCD(max(b1, b2), min(b1, b2))
A = a1 * (b2 // gcd) + a2 * (b1 // gcd)
B = b2 // gcd * b1
gcd = GCD(B, A)
print(A // gcd, B // gcd)
