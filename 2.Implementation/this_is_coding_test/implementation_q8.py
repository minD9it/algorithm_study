alpha_digit = input()

digit_sum = 0
alpha_list = []

for i in alpha_digit:
    if i.isdigit():
        digit_sum += int(i)
    elif i.isalpha():
        alpha_list.append(i)
1
alpha_list.sort()
alpha_list.append(str(digit_sum))
print(''.join(alpha_list))