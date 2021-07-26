import sys
read = sys.stdin.readline

n, k = map(int,read().split())
result = 0
word = []
for i in range(n):
    word.append(list(map(str,read())))
    word[i].pop()

def find(num,position):
    global result
    if num > k:
        return
    if num == k:
        numbersKnow=0
        for wo in word:
            for j in wo:
                if not learned[(ord(j)-97)]:
                    break
            else:
                numbersKnow += 1
        result = max(result,numbersKnow)
        return

    for i in range(position,26):
        if not learned[i]:
            learned[i]=True
            find(num+1,i)
            learned[i]=False

learned = [False]*26
learned[ord('a')-97] = True
learned[ord('c')-97] = True
learned[ord('i')-97] = True
learned[ord('n')-97] = True
learned[ord('t')-97] = True


if k < 5:
    print('0')
elif k>=26:
    print(n)
else:
    find(5, 0)
    print(result)



