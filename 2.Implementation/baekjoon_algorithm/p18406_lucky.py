n = input() # string type

sum1 = [int(i) for i in n[:int(len(n)/2)]]
sum2 = [int(i) for i in n[int(len(n)/2):]]

if sum(sum1) == sum(sum2):
    print('LUCKY')
else:
    print('READY')