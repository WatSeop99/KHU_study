'''
기본 아이디어 :
    정렬 알고리즘을 이용하는 문제인만큼, 수를 받아 정렬시킨다.
    후 출력
'''

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
    
def comp(a, b):
    return a > b

arr = sorted(arr, reverse = True)

for i in arr:
    print(i, end = ' ')