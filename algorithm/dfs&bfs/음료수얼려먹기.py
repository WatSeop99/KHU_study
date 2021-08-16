'''
기본 아이디어 : 
    아이스크림은 주어진 구멍의 경계로 결정된다. 따라서 붙어있는 구멍중 그 경계가 어디까지인가가 중요하다.
    이를 확인하는 가장 좋은 방법은 dfs(깊이 우선탐색)를 이용하는 것이다.
    이중 for문을 통해 dfs함수를 실행하여 연결되어있는 구멍경계를 파악하여,
    갯수에 추가한다.
'''

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# Dfs로 특정 노드 방문 후 연결된 모든 노드들도 방문
def Dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n: # 범위를 넘어가면
        return False
    if graph[x][y] == 0: # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1
        # 상, 하, 좌, 우 노드들을 확인
        Dfs(x - 1, y)
        Dfs(x, y - 1)
        Dfs(x + 1, y)
        Dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n): # 칸 하나하나 살펴보면서 카운트 됬나 확인
    for j in range(m):
        if Dfs(i, j) == True:
            result += 1

print(result)