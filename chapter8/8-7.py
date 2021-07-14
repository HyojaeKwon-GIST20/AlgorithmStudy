#개미 전사
import sys
read = sys.stdin.readline
n = int(read())
array = list(map(int,read().split()))

dp = [0]*100
dp[0] = array[0]
dp[1] = max(array[1],array[0])

for i in range(2,n):
    dp[i] = max(dp[i-1],array[i]+dp[i-2])

print(dp[n-1])