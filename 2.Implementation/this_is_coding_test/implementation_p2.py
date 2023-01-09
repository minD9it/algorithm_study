# input -> 00:00:00 ~ n:59:59
n = int(input())

count  = 0
current_time = [0, 0, 0] # [h, m, s]

for h in range(n+1): # 0 ~ n시간
    for m in range(60): # 60분 -> 0 ~ 59분
        for s in range(60): # 60초 -> 0 ~ 59초
            if '3' in ':'.join([str(i) for i in current_time]):  # 'h:m:s' -> string type
                count += 1
            current_time[2] += 1
        
        # 시간이기 때문에 60초 -> 1분
        if current_time[2] == 60:
            current_time[1] += 1
            current_time[2] = 0
    # 60분 -> 1시간
    if current_time[1] == 60:
        current_time[0] += 1
        current_time[1] = 0

print(count)