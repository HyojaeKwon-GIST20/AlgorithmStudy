import sys
read = sys.stdin.readline

number= read()

zero = 0
one = 0
if number[0] == '1':
    one+=1
else:
    zero+=1

for i in range(1,len(number)-1):
    if number[i-1] != number[i]:
        # print(number[i])
        if number[i] == '1':
            one+=1
        else:
            zero+=1
        # print(one,zero)
    # if i == len(number)-1:
print(min(one,zero))

