import sys
read = sys.stdin.readline
n = int(read())
def fivo(final):
    dp = [0, 1, 1]
    count = 1
    where = 2
    last = dp[1]
    while count<final:

        count= count + 1
        if where == 0:
            dp[1] = dp[0]+dp[2]
            last = dp[1]
        elif where ==1:
            dp[2] = dp[0]+dp[1]
            last = dp[2]
        else:
            dp[0] = dp[1]+dp[2]
            last = dp[0]
        where += 1
        if where >=3:
            where = 0
    return last
if n == 0:
    print(0)
elif n == 1 or n ==2:
    print(1)
else:
    print(fivo(n))