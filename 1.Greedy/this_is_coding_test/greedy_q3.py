s = input()

# flag = 1 연속해서 나타나고 있음 flag = 0 끊김
flag = 0

# 처음 값 저장 
init = s[0]

# 연속된 0, 연속된 1
cnt_0 = cnt_1 = 0

# 모든 원소 방문해서 확인
for i in s:
    if i == init and flag == 0:
        cnt_0 += 1
        flag = 1

    elif i != init and flag == 1:
        cnt_1 += 1
        flag = 0

print(cnt_0 if cnt_0 < cnt_1 else cnt_1)