'''
기본 아이디어 : 
    목적지까지의 최단거리를 구하는 문제이다. 이는 인접한 노드들을 탐색하여 목적지까지 가까운 거리를 찾아야 한다.
    이를 위해 bfs(너비우선탐색)를 이용한다.
    1. 현재 노드에서 인접한 노드들을 저장한 후
    2. 현재 노드가 적합한지 확인하고 적합하다면 거리를 저장, 큐에 인접 노드들을 넣는다. 적합하지 않다면 큐에서 꺼내 연산을 시행한다.
    3. 목적지는 맵의 끝이므로, 끝값을 반환한다.
'''

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 상, 하, 좌, 우를 위한 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def Bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 현재 위치에서 상, 하, 좌, 우로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 맵 범위를 벗어나면
                continue
            if graph[nx][ny] == 0: # 벽인경우
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1] # 가장 오른쪽 까지의 최단거리 반환

print(Bfs(0, 0))