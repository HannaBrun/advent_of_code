values = []
with open('calibration_values.txt', 'r') as file:
    for line in file.readlines():
        digits = list(filter(
            lambda it: it.isnumeric(),
            line
        ))
        values.append(int(f'{digits[0]}{digits[-1]}'))

print(sum(values))
