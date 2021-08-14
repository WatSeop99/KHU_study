'''
기본 아이디어 : 
    현재 위치에서 갈 수 있는 좌표들을 하나씩 둘러보며 갈 수 있는지 검사한다.
'''

step = [[2, -1], [2, 1], [-2, -1], [-2, 1], [-1, 2], [1, 2], [-1, -2], [1, -2]] # 갈 수 있는 이동좌표

data = input() # 현재 위치
y = int(data[1])
x = int(ord(data[0])) - int(ord('a')) + 1
count = 0

for i in range(8): # 갈 수 있는 이동좌표를 모두 확인
    nextX = x + step[i][0]
    nextY = y + step[i][1]
    if nextX >= 1 and nextX <= 8 and nextY >= 1 and nextY <= 8: # 범위 안에 갈 수 있다면
        count += 1
        
print(count)