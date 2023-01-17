# 모험가
n = int(input())

# 공포도
thrills = list(map(int, input().split()))

# 내림차순 -> 공포도가 많은 순서
thrills.sort(reverse=True)

groups = 0
person_n = 0

for th in thrills:
    person_n += 1
    if th <= person_n:
        groups += 1
        person_n = 0
        
print(groups)