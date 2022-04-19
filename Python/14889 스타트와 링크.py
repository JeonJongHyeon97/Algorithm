# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:56:44 2021

@author: JongHyeon
"""

#Brute Force

from itertools import combinations 
n = int(input()) 
s = [list(map(int, input().split())) for _ in range(n)] 
cb = combinations(range(n), n//2) 
ans = 9999
for c in cb: 
    start = c 
    link = list(set(range(n)) - set(c)) 
    start_power, link_power = 0, 0 
    for i in range(n//2 - 1): 
        for j in range(i + 1, n//2): 
            start_power += s[start[i]][start[j]] + s[start[j]][start[i]] 
            link_power += s[link[i]][link[j]] + s[link[j]][link[i]] 
    ans = min(ans, abs(link_power - start_power)) 
print(ans)

    