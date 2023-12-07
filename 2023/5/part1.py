from collections import OrderedDict, UserDict

class AlmanacMap(UserDict):

    def __setitem__(self, key: tuple, destination: int):
        source, length = key
        self.data[range(source, source+length)] = destination - source

    def __getitem__(self, key: int):
        for source_range, destination in self.data.items():
            if key in source_range:
                return destination + key

        return key


with open('seed_almanac.txt', 'r') as file:
    current_map = None
    maps = OrderedDict()
    for line in file.readlines():
        if line.startswith('seeds: '):
            seeds = list(map(
                int,
                line.strip('seeds: ').split()
            ))
        elif line == '\n':
            continue
        elif line.endswith('map:\n'):
            current_map = line.strip(' map:\n')
            maps[current_map] = AlmanacMap()
        else:
            destination, source, length = list(map(int, line.split()))
            maps[current_map][(source, length)] = destination

    closest_location = 0
    for seed in seeds:
        location = seed
        for mapping in maps.values():
            location = mapping[location]

        closest_location = location if closest_location == 0 else min(closest_location, location)

print(closest_location)
