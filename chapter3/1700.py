import sys
read = sys.stdin.readline

n, m = map(int,read().split())

k = list(map(int,read().split()))
plug = []*3

result = 0
for i in range(m):
    if k[i] in plug:
        continue
    if len(plug) < n:
        plug.append(k[i])
    else:
        count = 0
        time = []
        for j in range(len(plug)):
            phase = False
            # print(plug[j])
            for jj in range(i, m):
                if k[jj] == plug[j]:
                    # print(jj - (i-1))
                    # print(k[jj])
                    # print(i)
                    # print(j)
                    phase = True
                    # print(k[jj])
                    count = jj-i+1
                    time.append((count,j))
                    break
                        # time = j;
            if phase == False:
                time.append((101,j))
        # print(time)
        time = sorted(time,key=lambda time: time[0],reverse=True)

        # print(time[0])
        # print(i)
        plug[time[0][1]] = k[i]

        result += 1
    # print(plug)
print(result)

