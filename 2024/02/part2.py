from itertools import pairwise, starmap, filterfalse, compress


def is_safe(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    diff = starmap(lambda x, y: abs(x - y), pairwise(report))
    if list(filterfalse(lambda it: 0 < it < 4, diff)):
        return False
    
    return True


def main():
    with open('2024/02/input.txt', 'r') as fp:
        lines = fp.readlines()

    count = 0
    for line in lines:
        report = list(map(lambda el: int(el), line.split()))
        if is_safe(report):
            count += 1
            continue
        
        selector = [1] * len(report)
        for i in range(len(report)):
            selector[i] = 0
            if is_safe(list(compress(report, selector))):
                count += 1
                break
            selector[i] = 1

    return count


if __name__ == '__main__':
    count = main()
    print(count)
