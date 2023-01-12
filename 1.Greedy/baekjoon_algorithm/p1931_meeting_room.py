import numpy as np

# 회의 수
meeting = int(input())

# 각 회의의 시작 시간과 끝나는 시간
meeting_time = []
for i in range(meeting):
    meeting_time.append(list(map(int, input().split())))
print(meeting_time)

# 오름차순 정렬
meeting_time = np.unique(meeting_time, axis=0)
print(meeting_time)

maximum_meeting = 0

start = meeting_time.T[0]
print(start)


# # 많은 회의를 진행하기 위해서는 회의 시간이 적은 회의를 우선순위로 하면 됨
# meeting_duration  = []
# for m in meeting_time:
#     meeting_duration.append(m[1] - m[0]) # 회의 시간 구하기