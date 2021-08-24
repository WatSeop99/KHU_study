'''
기본 아이디어 :
    문제는 k번을 방문한 후, x번까지의 최소거리를 묻고있다.
    이는 플로이드 워셜 알고리즘에 가장 부합한다.
    이를 이용하여 구현한다.
'''

INF = int(1e9) # 무한을 의미하는 값

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선에 대한 값 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())
# 점화식에 따라 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
distance = graph[1][k] + graph[k][x] # 결과
if distance >= INF:
    print("-1")
else:
    print(distance)