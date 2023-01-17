# 모험가
n = int(input())

# 공포도
thrills = list(map(int, input().split()))

# 내림차순 -> 공포도가 많은 순서
thrills.sort(reverse=True)

groups = 0
flag = len(thrills)
i = 0
while flag < 1:
    flag -= thrills[i]
    groups += 1
    i += thrills[i]

print(groups)