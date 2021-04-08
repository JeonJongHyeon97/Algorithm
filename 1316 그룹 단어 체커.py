# -*- coding: utf-8 -*-
"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""
# 문자를 한글자씩 쪼개서 다른 리스트에 넣으며, 연속되는지 이미 리스트에 있는지 확인

case = int(input())
count = 0
test = []
for i in range(case):
    a = list(map(str, input()))  # 단어를 문자로 쪼개서 리스트화 ex) h a p p y
    for ii in range(len(a)):  # 하나씩 꺼내서 test에 있는지 확인하며 추가
        if a[ii] not in test or a[ii] == test[-1]:
            test.append(a[ii])
        else:
            test.append(0)
    if 0 not in test:
        count += 1  # 이상 없이 모두 추가한 경우
    test = []  # 리스트 초기화
print(count)