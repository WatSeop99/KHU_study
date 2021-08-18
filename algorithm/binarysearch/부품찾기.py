'''
기본 아이디어 :
    상점에 있는 부품중 고객이 원한 부품이 있는지를 찾아야 하는 탐색 문제이므로
    이진탐색을 이용하여 시간 안에 빠른 답을 낼 수 있도록 한다.
'''

def BinarySearch(arr, target):
    begin = 0
    end = len(arr)-1
    while begin <= end:
        mid = (begin+end)//2
        if arr[mid] < target:
            begin = mid+1
        elif arr[mid] > target:
            end = mid-1
        else:
            return mid
    return None

n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))

store.sort()
for i in range(m):
    result = BinarySearch(store, customer[i])
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')