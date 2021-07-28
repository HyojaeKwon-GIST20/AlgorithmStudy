import sys
read = sys.stdin.readline

k = int(read())
dp=[]
dp.append(0)
for i in range(k):
    dp.append(int(read()))
anp = []
anp.append(0)
while True:
    anp.append(dp[1])
    if k == 1:
        break
    anp.append(max(dp[2],dp[2]+dp[1]))
    if k == 2:
        break
    anp.append(max(dp[3]+dp[2],dp[3]+dp[1]))
    if k >= 3:
        break
if k <= 3:
    print(anp.pop())
else:
    for i in range(4,k+1):
        anp.append(max(dp[i]+anp[i-2],dp[i]+dp[i-1]+anp[i-3]))
    print(anp.pop())