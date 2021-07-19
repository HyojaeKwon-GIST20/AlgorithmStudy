import sys
read = sys.stdin.readline

n = int(read())
con = []
for i in range(n):
   j, k = map(int,read().split())
   j=int(j)
   k=int(k)
   con.append([j,k])

con = sorted(con,key=lambda con: (con[1],con[0]))

# print(con)
count = 1
end = con[0][1]
for i in range(1,n):
    if con[i][0] >= end:
        count = count + 1
        # print(con[i])
        end = con[i][1]

print(count)