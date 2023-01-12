columns = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
}

start_position = [i for i in input()] # 열, 행
start_position[0] = columns.get(start_position[0])

# (열, 행)
moving_cases = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cases_count = 0

for c, r in moving_cases:
    move_c = int(start_position[0]) + c
    move_r = int(start_position[1]) + r
    if move_r > 0 and move_r < 9 and move_c > 0 and move_c < 9:
        cases_count += 1

print(cases_count)