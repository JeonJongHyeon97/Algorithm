import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
recommend = list(map(int, input().split()))
cnt = {}
cache = []

for i in recommend:
    if len(cache) < n or (len(cache)==n and i in cache):
        if i not in cnt.keys():
            cache.append(i)
            cnt[i]=1
        else:
            cnt[i]+=1
    else:
        minList = []
        for key in cnt.keys():
            if cnt[key] == min(cnt.values()):
                minList.append(key)
        for j in cache:
            if j in minList:
                cache.remove(j)
                del cnt[j]
                break
        cache.append(i)
        cnt[i]=1

print(*sorted(cache))

