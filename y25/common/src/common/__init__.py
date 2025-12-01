def parse_file(day: str) -> str:
    with open(f'days/{day}/input', 'r') as file:
        data = file.read()
    
    return data
