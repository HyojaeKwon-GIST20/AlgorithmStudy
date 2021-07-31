import sys
read = sys.stdin.readline

n = int(read())
dp = []
arr = list(map(int,read().split()))
dp = [1]*n

arr.reverse()
max_num = 1
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
        if dp[i] > max_num:
                max_num=dp[i]
print(n-max_num)
