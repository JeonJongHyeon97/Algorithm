import sys
input = sys.stdin.readline
n = int(input())

count=0
def num(number, start):
    global count
    number.append(start)
    if len(number) == n:
        count+=1
        return
    else:
        if start != 0:
            num(number,start-1)
        if start != 9:
            num(number, start+1)


for i in range(1,10):
    number=[]
    num(number,i)

print(count)