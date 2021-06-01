# -*- coding: utf-8 -*-
"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""
# 팩토리얼을 구하는 함수를 정의한 후, 0의 갯수 구하기

def fac(n):
    if n==1 or n == 0:
        return 1
    else:
        return n*fac(n-1)   # 재귀를 이용
    
n = int(input())
n = str(fac(n))
i=-1
count=0
while n[i]=="0":    # 뒤에서 부터 0의 개수 구하기
    i-=1
    count+=1
print(count)