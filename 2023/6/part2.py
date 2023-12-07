with open('record_distances.txt', 'r') as file:
    time = int(''.join(file.readline().strip('Time:').split()))
    record = int(''.join(file.readline().strip('Distance:').split()))

    nbr_of_ways_to_win = 0
    for charge in range(1, time):
        if charge * (time - charge) > record:
            nbr_of_ways_to_win += 1

    print(nbr_of_ways_to_win)
