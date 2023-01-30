str_input = input()

result = 0
for i in str_input:
    if result == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)