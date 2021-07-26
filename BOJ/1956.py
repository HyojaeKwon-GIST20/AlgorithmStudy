import sys
read = sys.stdin.readline
INF = int(1e9)

v, e = map(int,read().split())

final_graph = [[INF]*v for _ in range(v)]

for i in range(e):
    a ,b, c = map(int,read().split())
    final_graph[a-1][b-1] = c

for i in range(v):
    for j in range(v):
        for k in range(v):
            if final_graph[j-1][k-1] >final_graph[j-1][i-1] + final_graph[i-1][k-1]:
                final_graph[j-1][k-1] = final_graph[j-1][i-1] + final_graph[i-1][k-1]

result = INF
for i in range(v):
    result = min(result,final_graph[i][i])
if result == INF:
    print('-1')
else:
    print(result)