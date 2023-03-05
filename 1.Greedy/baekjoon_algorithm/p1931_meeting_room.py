# # 회의 수
# meeting = int(input())

# # 각 회의의 시작 시간과 끝나는 시간
# meeting_time = []
# for i in range(meeting):
#     meeting_time.append(list(map(int, input().split())))

# # 오름차순 정렬
# meeting_time.sort()

# # 내림차순 정렬
# meeting_time.reverse()

# current = meeting_time[0]
# count = 1
# for i, mt in enumerate(meeting_time[1:], 1):
#     if meeting_time[i][1] <= current[0] and meeting_time[i][0] < current[1]: # 
#         count += 1
#         current = mt

# print(count)

n = int(input()) # 회의 개수
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0])) # key 우선순위 -> 끝나는 시간으로 정렬 ~ 시작 시간 정렬 ex) [1, 4], [2, 4] 이런식
print(time)

ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)