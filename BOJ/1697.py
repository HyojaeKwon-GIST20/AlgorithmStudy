#수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

import sys
from collections import deque
INF = int(1e9)

read = sys.stdin.readline
graph = [INF]*100001
n, k = read().split()
n = int(n)
k = int(k)
queue = deque()
queue.append(n)
graph[n] = 0

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()

        if x == k:
            return
        for i in (x+1,x-1,x*2):
            if 0 <= i <= 100000 and graph[i] ==INF :
                graph[i] = graph[x]+1
                queue.append(i)

bfs(n)
print(graph[k])
# numbers = ['one', 'two', 'three', 'four', 'five']
#
# for n in numbers:
#     print(n)