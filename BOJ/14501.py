import sys
read = sys.stdin.readline
tesk = []

n = int(read())
ans = [0]*(n+5)

for i in range(n):
    tesk.append(map(int,read().split()))
maxi = 0
for i in range(n):
    day, money = tesk[i]
    if i+day <= n+1:
        ans[i+day] = max(ans[i]+money,ans[i+day])
    ans[i+1] = max(ans[i],ans[i+1])
    maxi= max(ans[i+1],maxi)

print(maxi)


