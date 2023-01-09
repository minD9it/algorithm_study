# n X n matrix
n = int(input())

# 이동 계획서
moving_plan = list(input().split())

# 시작 위치 
x, y = 1, 1 # 행, 열

# moving plan에 따라서 움직이기 시작함
for move in moving_plan:
    if move  == 'L':
        temp = y - 1
        if temp <= 0:
            continue
        else:
            y = temp
    elif move == 'R':
        temp = y + 1
        if temp > n:
            continue
        else:
            y  = temp
    elif move == 'U':
        temp = x - 1
        if temp <= 0:
            continue
        else:
            x = temp
    elif move == 'D':
        temp = x + 1
        if temp > n:
            continue
        else:
            x = temp

print(x, y)