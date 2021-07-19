import sys
read = sys.stdin.readline

n,m,k = map(int,read().split())
graph = list(map(int,read().split()))
flag_graph = [False]*k
point_stack = 0
min = int(1e9)

for i in range(k):
    num_1 = graph
    for j in range(i,k):



