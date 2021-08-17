'''
기본 아이디어 :
    한쪽은 오름차순으로, 다른 한쪽은 내림차순으로 정렬.
    가장 작은 원소와 가장 큰 원소를 교환. 이때 가장 작은 원소는 가장 큰 원소보다 작아야함.
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))