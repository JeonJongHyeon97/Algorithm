# -*- coding: utf-8 -*-
"""
올바른 배열이란 어떤 배열 속에 있는 원소 중 5개가 연속적인 것을 말한다. (연속적인 것이란 5개의 수를 정렬했을 때, 인접한 수의 차이가 1인 것을 말한다.)

예를 들어 배열 {6, 1, 9, 5, 7, 15, 8}은 올바른 배열이다. 왜냐하면 이 배열 속의 원소인 5, 6, 7, 8, 9가 연속이기 때문이다.

배열이 주어지면, 이 배열이 올바른 배열이 되게 하기 위해서 추가되어야 할 원소의 개수를 출력하는 프로그램을 작성하시오.
"""
# 주어진 수의 -4부터 +4 까지 5개씩 끊어서 가지고 있는지 확인하며 최소값을 찾는다.

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num=sorted(num)
answer=[]
for i in num:
    # print("i : ",i)
    for j in range(-4,1):
        plus=0
        # print("j : ",j)
        for k in range(0,5):
            # print("k : ",k)
            # print("total : ",i+j+k)
            if i+j+k not in num:
                plus+=1
        answer.append(plus)
        
print(min(answer))



