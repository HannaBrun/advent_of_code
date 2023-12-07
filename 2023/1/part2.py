str_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def digitize_string(string: str):
    for key, value in str_digits.items():
        string = string.replace(key, f'{key[0]}{value}{key[-1]}')

    return string


values = []
with open('calibration_values.txt', 'r') as file:
    for line in file.readlines():
        digitized_line = digitize_string(line)
        digits = list(filter(
            lambda it: it.isnumeric(),
            digitized_line
        ))
        values.append(int(f'{digits[0]}{digits[-1]}'))

print(sum(values))
