from itertools import pairwise, starmap, filterfalse

with open('2024/02/input.txt', 'r') as fp:
    lines = fp.readlines()

count = 0
for line in lines:
    report = list(map(lambda el: int(el), line.split()))

    if sorted(report) != report and sorted(report, reverse=True) != report:
        continue

    diff = starmap(lambda x, y: abs(x - y), pairwise(report))
    if list(filterfalse(lambda it: 0 < it < 4, diff)):
        continue

    count += 1

print(count)
