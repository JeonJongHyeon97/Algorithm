# -*- coding: utf-8 -*-

# 규칙 찾기


import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
cursor = 0
noAns=True
if n == 1:
    print(-1)
else:
    for i in range(n - 1, 0, -1):
        if s[i - 1] < s[i]: # 뒤에서 부터 처음으로 오른차순 순열이 나타나는 지점 한칸 앞을 커서로 지정==> 바꿔줘야 하는 자리
            cursor = i - 1
            break
    for i in range(n - 1, 0, -1):
        if s[cursor] < s[i]:    # 뒤에서 부터 처음으로 커서보다 큰값을 찾아서 커서 자리와 값 바꾸기
            s[cursor], s[i] = s[i], s[cursor]
            s = s[:cursor + 1] + sorted(s[cursor + 1:]) # 커서자리 까지는 그대로, 그다음 부터는 재정렬 시켜주기
            print(*s)
            break
        if i == 1:
            print(-1)
        