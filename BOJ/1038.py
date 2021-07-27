import sys
def decreasingNum(num):
    cur = 0
    k=0
    while True:
        if cur == num:
            print(k)
            return
        else:
            flag = False
            str_k = str(k)
            for i in range(len(str_k)-1,0,-1):
                if int(str_k[i]) < int(str_k[i-1]):
                    cur += 1
                    print(cur)
                    continue
                else:
                    num_k = str_k[i-1]
                    print(num_k,str_k[i],k)
                    while True:
                        k+=1
                        str_k = str(k)
                        if str_k[i] >= num_k:
                            break
                    flag = True
                    break
        k += 1
num = int(sys.stdin.readline())
decreasingNum(num)


