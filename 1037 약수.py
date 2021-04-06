# -*- coding: utf-8 -*-
"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
"""

# 주어진 약수중 최솟값과 최댓값을 곱하면 된다.

n = int(input())
num_list = list(map(int, input().split()))

print(max(num_list) * min(num_list))
