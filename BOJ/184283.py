import sys
read = sys.stdin.readline
from collections import deque

n= int(read())
graph=[]
teach = []
for i in range(n):
    graph.append(list(map(str,read().split())))
    for j in range(n):
        if graph[i][j]=='T':
            teach.append((i,j))

k = 0
dx = [1,-1,0,0]
dy=[0,0,1,-1]

def find(teach):
    qu = deque(teach)
    while qu:
        x,y = deque.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 'X'
                else:

def ans(count):
    if count == 3:
