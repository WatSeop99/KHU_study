'''
기본 아이디어 : 
    한 도시에서 다른 도시까지의 최단거리로 문제를 볼 수 있다.
    다익스트라 알고리즘을 이용하여 구현한다.
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한값

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # x번 노드에서 y번 노드로 가는 비용이 z

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 빌때까지 반복
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
count = 0 # 도달할 수 있는 노드의 개수
max_distance = 0 # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)