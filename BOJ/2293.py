import sys
read = sys.stdin.readline

dp = [0]*10001

n,k = (read().split())
n = int(n)
k = int(k)
coin = [0] * 3

for i in range(n):
    c = read()
    c = int(c)
    coin[i] = c

dp[0] = 0
# print(coin)
for i in range(n):
    for j in range(coin[i],k+1):
        dp[j] = max(dp[j],dp[j-coin[i]]+1)
if dp[k] == 0:
    print("-1")
else:
    print(dp[k])

