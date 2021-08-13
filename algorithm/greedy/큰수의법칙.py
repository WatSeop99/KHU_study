'''
기본 아이디어 : 
    가장 큰 수를 만들기 위해서는
    1. 주어진 배열 중 가장 큰 두 수를 뽑는다.
    2. 가장 큰 수를 k번씩 더하고 사이에 작은 수를 더한다.
2번 과정 최적화
==> 더해지는 수들(첫번째로 큰 수 + 두번째로 큰 수)이 반복된다. 반복되는 수들의 횟수 계산하면 반복문을 쓰지 않아도 된다(상수시간으로 처리 가능).
    반복하여 더해지는 수는 k+1이므로 m을 k+1로 나눈 수만큼 배열이 더해진다.
'''
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
num1 = arr[n-1] # 첫번째로 큰 수
num2 = arr[n-2] # 두번째로 큰 수

count = int(m / (k + 1)) * k + m % (k + 1) # 가장 큰 수가 더해지는 횟수

result = count * num1
result += (m - count) * num2

print(result)