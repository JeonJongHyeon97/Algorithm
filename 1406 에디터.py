# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Wed May 26 11:05:01 2021

@author: user
"""

=======
Created on Sun May 30 14:45:55 2021

@author: JongHyeon
"""
#insert 보다 직접 slicing이 더 빠름

import sys 
input=sys.stdin.readline
left_stack = list(input()) 
right_stack = []
m = int(input()) 
for _ in range(m): 
    cmd = input()
    if cmd[0] == 'L' and left_stack: 
        right_stack.append(left_stack.pop()) 
    elif cmd[0] == 'D' and right_stack: 
        left_stack.append(right_stack.pop()) 
    elif cmd[0] == 'B' and left_stack: 
        left_stack.pop() 
    elif cmd[0] == 'P': 
        left_stack.append(cmd[2]) 
    print()
    print(''.join(left_stack + right_stack[::-1]))

print(''.join(left_stack + right_stack[::-1]))
>>>>>>> 713e73ee0d51389685ead9fe449010bfc2a9301b
