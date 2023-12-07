def cumsum(array):
    res = 1
    for el in array:
        res *= el

    return res

with open('record_distances.txt', 'r') as file:
    times = list(map(int, file.readline().strip('Time:').split()))
    records = list(map(int, file.readline().strip('Distance:').split()))

    values_to_multiply = []
    for time, record in zip(*(times, records)):
        nbr_of_ways_to_win = 0
        for charge in range(1, time):
            if charge * (time - charge) > record:
                nbr_of_ways_to_win += 1

        values_to_multiply.append(nbr_of_ways_to_win)

    print(cumsum(values_to_multiply))
