'''
기본 아이디어 :
    이진탐색을 응용하여 절단기 높이의 최댓값을 구한다.
    이때, 절단기의 높이를 찾는게 아니라 절단기의 높이를 중간값으로 하되, 
    잘려나간 떡의 길이가 m값과 같은지 비교하면서 탐색을 진행한다.
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
begin = 0
end = max(arr)
result = 0
while begin <= end: # 이진 탐색
    mid = (begin+end)//2
    total = 0 # 잘려나갈 부분
    for i in arr: # 기준이 해당 떡보다 작다면 자름
        if mid < i:
            total += i-mid
    if total < m: # m 미만이라면 범위 다시설정
        end = mid-1
    else:
        result = mid
        begin = mid+1
print(result)