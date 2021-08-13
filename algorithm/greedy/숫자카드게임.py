'''
기본 아이디어 :
    문제에서 요구하는 조건들은 다음과 같다.
    1. 행에서 가장 작은 수를 고를 것.
    2. 작은 수들 중 가장 큰 수를 고를 것.
    반복문을 통해 위 조건들을 실행한다.
'''


n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_ = min(arr) # 행에서 가장 작은 수
    result = max(result, min_) # 작은 수들 비교

print(result)