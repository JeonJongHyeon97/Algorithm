n = int(input())
outputList=[]

for _ in range(n):
    outputList.append(int(input()))
        
inputList=[i for i in range(n,0,-1)]
stack=[0]
answer=[]
remove=[]
now=1

for i in outputList:
    if i > stack[-1] and i not in remove:
        while stack[-1]<i:
            stack.append(inputList.pop())
            answer.append("+")
        remove.append(stack.pop())
        answer.append("-")
    elif i <= stack[-1] and i in stack:
        while stack[-1] > i-1:
            remove.append(stack.pop())
            answer.append("-")
    else:
        answer="NO"
        break

if answer != "NO":
    for i in answer:
        print(i)
else:
    print(answer)
