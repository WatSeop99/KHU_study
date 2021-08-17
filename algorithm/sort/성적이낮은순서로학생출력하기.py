'''
기본 아이디어 : 
    학생 이름과 성적을 한 pair로 입력받아 점수를 기준으로 정렬함.
    파이썬 문법과 정렬 함수 사용법 잘 알아둘것.
'''

n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))
    
def comp(data):
    return data[1]

arr = sorted(arr, key = comp)
for i in arr:
    print(i[0], end = ' ')