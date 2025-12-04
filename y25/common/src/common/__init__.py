def clamp(n, min_, max_):
    return max(min_, min(n, max_))

def parse_file(day: int) -> str:
    with open(f'days/d{day}/input', 'r') as file:
        data = file.read()
    
    return data
