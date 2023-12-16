
class Galaxy:
    def __init__(self, point: tuple) -> None:
        self.point = point

    def adjust_coordinates(self, rows, columns) -> None:
        x = 0
        y = 0
        for row in rows:
            if row <= self.point[1]:
                y += 1
        for column in columns:
            if column <= self.point[0]:
                x += 1

        self.point = (self.point[0] + x, self.point[1] + y) 

    def __eq__(self, other) -> bool:
        return self.point == other.point

    def __sub__(self, other):
        return sum(
            (abs(self.point[0] - other.point[0]), abs(self.point[1] - other.point[1]))
        )

    def __repr__(self) -> str:
        return f'{self.point}'

with open('galaxies.txt', 'r') as file:
    galaxies = []
    empty_rows = []
    empty_columns = []  
    for y, line in enumerate(file.readlines()):
        row = line.strip('\n')

        # record empty rows and columns
        if not row.strip('.'):
            empty_rows.append(y)
        empty_this_line = {x for x, el in enumerate(row) if el =='.'}
        if y == 0:
            empty_columns = empty_this_line
        else:
            empty_columns &= empty_this_line

        # find galaxies
        galaxies.extend([
            Galaxy((x, y)) for x, el in enumerate(row) if el =='#'
        ])

    for galaxy in galaxies:
        galaxy.adjust_coordinates(empty_rows, empty_columns)

    distances = 0
    for i, galaxy in enumerate(galaxies):
        for other in galaxies[i+1:]:
            distances += (galaxy - other)

    print(distances)
