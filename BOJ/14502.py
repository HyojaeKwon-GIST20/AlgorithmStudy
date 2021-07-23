import sys
from collections import deque
read = sys.stdin.readline

graph =[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,read().split())
for i in range(n):
    graph.append(list(map(int,read().split())))
maxResult = 0

def bfs(graph):
    global maxResult
    queue = deque()
    wall_graph=[[0]*m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 2:
                queue.append((i,j))
                wall_graph[j][i] = 2
            if graph[j][i] == 1:
                wall_graph[j][i] = 1

    while queue:
        x,y  = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<= ny<n and wall_graph[ny][nx] == 0:
                wall_graph[ny][nx] = 2
                queue.append((nx,ny))
    count = 0
    for j in range(n):
        for i in range(m):
            if wall_graph[j][i] == 0:
                count += 1
    maxResult = max(count, maxResult)

    return count

def bfCreateWall(times):
    if times == 3:
        bfs(graph)
        return
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 0:
                graph[j][i] = 1
                bfCreateWall(times+1)
                graph[j][i] = 0


bfCreateWall(0)
print(maxResult)


