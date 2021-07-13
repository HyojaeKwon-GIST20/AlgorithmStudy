import heapq
import sys

INF = int(1e9)

#노드의 개수, 간선 개수 입력받기
n, m = map(int,sys.stdin.readline().split())
#시작 노드 번호를 입력받기
start = int(sys.stdin.readline())
#각 노드에 연결돼 있는 노드에 대한 정보를 담는 리스트 만들기
graph =[[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * ( n + 1 )

#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijstra(start):
    q = []
    heapq.heappush(q, (0 , start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('No')
    else:
        print(distance[i])
