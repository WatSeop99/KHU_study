'''
기본 아이디어 : 
    다음과 같은 함수를 정의하고 동적할당을 실행한다.
    Money(lefted) = lefted만큼 돈이 남았을 때, 구성할 수 있는 화폐의 최소개수
    화폐 단위를 하나씩 순회하면서 각 단위로 최소개수를 낼 수 있는지를 탐색한다.
'''

n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))
cache = [10001] * (m + 1) # 메모이제이션을 위한 DP테이블

def Money(lefted): # 다이나믹 프로그래밍 진행.
    if lefted == 0:
        return 0
    if lefted < 0:
        return 10002
    if cache[lefted] != 10001:
        return cache[lefted]
    for i in range(n):
        cache[lefted] = min(cache[lefted], 1+Money(lefted-money[i]))
    return cache[lefted]

result = Money(m)
if result != 10001:
    print(result)
else:
    print(-1)