with open('2024/01/input.txt', 'r') as fp:
    data = fp.readlines()

left, right = [], []

for line in data:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

sum_ = 0
for l in left:
    sum_ += l * right.count(l)

print(sum_)
