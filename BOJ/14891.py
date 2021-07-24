import sys
read = sys.stdin.readline
from collections import deque

graph = []
time = []
graph =[deque(map(int,input())) for _ in range(4)]
graph = deque(graph)

times = int(read())

for i in range(times):
    time.append(list(map(int, read().split())))
time = deque(time)

while time:
    index , dir = time.popleft()
    index = index - 1
    left_tmp = graph[index][6]
    right_tmp = graph[index][2]
    graph[index].rotate(dir)

    t_dir = dir
    for i in range(index+1,4):

        if graph[i][6] != right_tmp:
            right_tmp =graph[i][2]
            t_dir *= -1
            graph[i].rotate(t_dir)
        else:
            break

    t_dir=dir
    for i in range(index-1,-1,-1):
    #for loop 에서 range(index-1,-1,-1)는 index-1에서 -1까지 거꾸로를 의미
        if graph[i][2] != left_tmp:
            left_tmp =graph[i][6]
            t_dir *= -1
            graph[i].rotate(t_dir)
        else:
            break

score = 0
for i in range(4):
    if graph[i][0] == 1:
        score += (2**i)
print(score)