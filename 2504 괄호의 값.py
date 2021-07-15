import sys

st = input().rstrip()
if "(]" in st or "[)" in st:
    print(0)
else:
    answer = 1
    st=st.replace('()', "2", 15)
    st=st.replace('[]', "3", 15)
    num = list(st)
    stack = []
    check = []
    for i in num:
        if i == '(':
            stack.append(i)
            check.append(')')
        elif i == '[':
            stack.append(i)
            check.append(']')
        elif i.isdigit():
            if len(stack) != 0 and stack[-1].isdigit():
                stack.append(str(int(i)+int(stack.pop())))
            else:
                stack.append(i)
        elif i == ')':
            if len(check) == 0 or check[-1] != ")":
                answer = 0
                break
            check.pop()
            tmp = 1
            if len(stack) != 0 and stack[-1].isdigit():
                tmp = int(stack.pop())
            stack.pop()
            if len(stack) != 0 and stack[-1].isdigit():
                stack.append(str(int(str(tmp*2))+int(stack.pop())))
            else:
                stack.append(str(tmp*2))

        elif i == ']':
            if len(check) == 0 or check[-1] != "]":
                answer = 0
                break
            check.pop()
            tmp = 1
            if len(stack) != 0 and stack[-1].isdigit():
                tmp = int(stack.pop())
            stack.pop()
            if len(stack) != 0 and stack[-1].isdigit():
                stack.append(str(int(str(tmp*3))+int(stack.pop())))
            else:
                stack.append(str(tmp*3))
    if answer != 0 and len(stack) == 1:
        print(stack[-1])
    else:
        print(0)
