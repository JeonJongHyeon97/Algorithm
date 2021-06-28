formula = input()
num = []
tmp = ""
sign = True
for i in range(len(formula)):
    now = formula[i]
    if now.isdigit():
        tmp += now
    elif num[i] == '-':
        num.append(int(tmp) if sign else -int(tmp))
        tmp = ''
        sign = True if now == '+' else False
        
    if i == len(formula)-1:
        num.append(int(tmp) if sign else -int(tmp))
