#모험가 길드
import sys
read = sys.stdin.readline

num = read()
number = list(map(int,read().split()))

number.sort()

count = 0
i = 0
while True:
    k = number[i]
    i = i + k
    print(i)
    if i >= len(number):
        break
    count+=1


print(count)
