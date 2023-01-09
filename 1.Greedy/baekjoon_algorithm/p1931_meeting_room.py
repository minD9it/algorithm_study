# 회의 수
meeting = int(input())

# 각 회의의 시작 시간과 끝나는 시간
meeting_time = []
for i in range(meeting):
    meeting_time.append(list(map(int, input().split())))

maximum_meeting = 0

# 많은 회의를 진행하기 위해서는 회의 시간이 적은 회의를 우선순위로 하면 됨
meeting_duration  = []
for m in meeting_time:
    meeting_duration.append(m[1] - m[0]) # 회의 시간 구하기


# 마지막 회의 시간을 기준으로 계산하는 것으로 해보자 
# numpy.unique를 사용하면 array 안에 리스트가 오름차순으로 정렬된다.
