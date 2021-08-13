'''
기본 아이디어 : 
    n이 1이 될 때까지 최소로 실행되기 위해서 조건 1을 최소화 해야한다.
    조건 2를 실행하기 위해서는 n이 k의 배수가 되야하므로
    조건 1을 실행하여 k의 배수로 n을 맞춰줘야 한다.
'''

n, k = map(int, input().split())

count = 0

forSub = n % k # 조건 1 실행 횟수
count += forSub
while n != 1: # 조건 2 실행 횟수
    n //= k
    count += 1

print(count)