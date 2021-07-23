import sys
read = sys.stdin.readline

dp = [0]*10001
dp[0] = 1

n,k = map(int,read().split())
coin = [0] * n

for i in range(n):
    c = int(read())
    coin[i] = c

for i in range(len(coin)):
     # j = 0
    for j in range(k+1):
        if j < coin[i]:
            continue
        dp[j] = dp[j] + dp[j-coin[i]]

print(dp[k])


