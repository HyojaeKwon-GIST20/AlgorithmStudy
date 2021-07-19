import sys
read = sys.stdin.readline

t = read()
for _ in range(t):
    n = read()
    graph = []
    for i in range(n):
        a, b = map(int,read().split())
        graph.append((a,b))
    graph = sorted(graph, key=lambda)
    sorted(time, key=lambda time: time[0], reverse=True)