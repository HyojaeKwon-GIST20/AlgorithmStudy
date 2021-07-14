import sys
read = sys.stdin.readline

n = int(read())

dp_table = [0]*30001

for i in range(2,n+1):
    dp_table[i]=dp_table[i-1]+1
    if dp_table[i] % 2 == 0:
        dp_table[i] = min(dp_table[i],dp_table[i//2]+1)
    if dp_table[i] % 3 == 0:
        dp_table[i] = min(dp_table[i],dp_table[i//3]+1)
    if dp_table[i] % 5 == 0:
        dp_table[i] = min(dp_table[i],dp_table[i//5]+1)
print(dp_table[n])
