# -*- coding: utf-8 -*-
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""

# 백트랙킹
# 파이썬 내의 중복없이 조합을 해주는 라이브러리를 사용해서 풀이도 가능
"""
from itertools import permutations
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str
"""




