## 큰 수의 법칙

# n, m, k
n, m, k = map(int, input().split())
# list
data = list(map(int, input().split()))

# ascending order ex) [1, 2, 3,...]
data.sort()
maximum1 = data[-1]
maximum2 = data[-2]

result = 0 
for i in range(0, m, k+1): # k+1 => (maximum1 + maximum1)(k) + maximum2(1)
  for j in range(k):
    result += maximum1
  result += maximum2
  
print(result)
