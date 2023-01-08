# 준규가 가지고 있는 동전의 종류
# 가장 적은 동전의 개수로 만들고자 하는 값
coin_type, want_sum = map(int, input().split())

# 동전의 값이 오름차순으로 주어짐
coins = []
for n in range(coin_type):
    coins.append(int(input()))

# 내림차순 정렬
coins.sort(reverse=True)

# 동전 개수 카운트
count = 0
# 큰 동전부터 시작
for c in coins:
    # 동전 추가
    count += want_sum // c
    # 남은 돈
    want_sum %= c

print(count)