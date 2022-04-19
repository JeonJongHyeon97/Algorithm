# -*- coding: utf-8 -*-
"""
네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.
"""

case = int(input())
def length(d1, d2):
    answer = ((d1[0]-d2[0])**2+(d1[1]-d2[1])**2)**(1/2)
    return answer

four=[]
two=[]
answer=[]
for _ in range(case):
    tmp=0
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    d3 = list(map(int, input().split()))
    d4 = list(map(int, input().split()))
    leng=[length(d1, d2),length(d1, d3),length(d1, d4),length(d2, d3),length(d2, d4),length(d3, d4)]

    for i in range(len(leng)):
        if leng.count(leng[i]) == 4:
            four.append(leng[i])
        elif leng.count(leng[i]) == 2:
            two.append(leng[i])
    if len(four)==4 and len(two)==2:
        if four[0]*(2**(1/2))==two[0]:
            print(1)
    else :
        print(0)

 
                









