'''
기본 아이디어 : 
    캐릭터가 갈 수 있는 곳을 카운트하는 문제이다.
    입력으로 받은 데이터를 맵과 캐릭터에 맞게 끔 초기화 해주고
    다음 분기과정을 반복하여 갈 수 있는 곳의 수를 센다.
    1. 왼쪽이 갈 수 있는 곳이면 이동하고 카운트
    2. 사방이 갈 수 없는 곳이면 뒤로 물러남. 이때 뒤로 물러날 곳이 바다면 반복 종료 
'''

mapX, mapY = map(int, input().split()) # 맵 좌표
x, y, dirc = map(int, input().split()) # 캐릭터 좌표 + 보는 방향
arr = [] # 맵
for i in range(mapX):
    arr.append(list(map(int, input().split())))
visit = [[0] * mapY for _ in range(mapX)] # 해당위치를 갔는가?
visit[x][y] = 1
step = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 북, 동, 남, 서 방향

count = 1 # 가본 곳 카운트
turn_count = 0
while True:
    turn_count += 1 # 일단 왼쪽을 확인
    dirc -= 1
    if dirc  == -1:
        dirc = 3
    moveOnX = x + step[dirc][0]
    moveOnY = y + step[dirc][1]
    if visit[moveOnX][moveOnY] == 0 and arr[moveOnX][moveOnY] == 0: # 왼쪽방향이 안 가본 곳이고, 육지인가?
        visit[moveOnX][moveOnY] = 1
        x = moveOnX
        y = moveOnY
        count += 1
        turn_count = 0
        continue
    if turn_count == 4: # 사방을 확인했지만 갈 수 없을 때
        nx = x - moveOnX
        ny = y - moveOnY
        if arr[nx][ny] == 0: # 육지라면 뒤로 물러남
            x = nx
            y = ny
            turn_count = 0
        else: # 바다면 종료
            break
        
print(count)