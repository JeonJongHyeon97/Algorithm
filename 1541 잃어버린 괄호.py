import sys
input = sys.stdin.readline
formula = input().rstrip()
num = []
ind = 0
sign = 1
for i in range(len(formula)):
    now = formula[i]
    if now == '+':
        num.append(sign*int(formula[i-ind:i]))
        ind = -1
    elif now == '-':
        num.append(sign*int(formula[i - ind:i]))
        sign = -1
        ind = -1
    if i == len(formula)-1:
        num.append(sign * int(formula[i - ind:i+1]))
    ind +=1
print(num)
print(sum(num))
