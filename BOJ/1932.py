import sys
read = sys.stdin.readline

n = int(read())
num = []
ans = [[0] * n for _ in range(n) ]
ans[0][0]
for _ in range(n):
    num.append(list(map(int,read().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            l = 0
        else:
            l = num[i-1][j-1]
        if j == i:
            u = 0
        else:
            u = num[i-1][j]
        num[i][j] = max(num[i][j]+u,num[i][j]+l)

print(max(num[n-1]))