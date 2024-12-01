with open('2024/01/input.txt', 'r') as fp:
    data = fp.readlines()

left, right = [], []

for line in data:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

sum_ = 0
for l, r in zip(sorted(left), sorted(right)):
    sum_ += abs(l - r)

print(sum_)
