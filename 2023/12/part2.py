import functools
import itertools
import re
from time import perf_counter as pf

# @functools.cache
def count_permutations(symbols, counts, group_loc=0):
    if not symbols:
        return not counts and not group_loc
    results = 0
    possibilities = ['.', '#'] if symbols[0] == '?' else [symbols[0]]
    for p in possibilities:
        if p == '#':
            results += count_permutations(symbols[1:], counts, group_loc + 1)
        else:
            if group_loc > 0:
                if counts and counts[0] == group_loc:
                    results += count_permutations(symbols[1:], counts[1:])
            else:
                results += count_permutations(symbols[1:], counts)
    return results

# def count_permutations(symbol, counts):
#     results = set()
#     possibilities = []
#     for s in symbol:
#         if s == '?':
#             possibilities.append(['#', '.'])
#         else:
#             possibilities.append([s])

#     # print(possibilities)

#     for combo in itertools.product(*possibilities):
#         candidate = ''.join(combo)
#         matches = re.findall(r'#+', candidate)
#         match_lengths = [len(x) for x in matches]
#         if match_lengths == counts:
#             results.add(candidate)

#     return len(results)

with open('condition.txt', 'r') as file:
    start = pf()
    count = 0
    for line in file.read().splitlines():
        springs, schema = line.split()
        schema = tuple([*map(int, schema.split(','))])
        count += count_permutations(springs + '.', schema)

    print(count)
    print(f'{pf() - start:.2f} s')


# class Combo:
#     def __init__(self, unknown_combos, unknowns, schema) -> None:
#         self.curr = 0
#         self.stop = unknown_combos
#         self.bits = unknowns
#         self.schema = schema

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.curr >= self.stop:
#             raise StopIteration

#         x = bin(self.curr)[2:].zfill(self.bits)
#         # Om '111' in x:
#         # Avancera fram self.curr så många steg som möjligt för att skippa följande tal med tre konsektuiva ettor.
#         # Annars
#         self.curr += 1

#         return x


# # @functools.cache
# def parse(possibility: list, schema):
#     output = [
#         str(len(springs_in_a_row)) if min(schema) <= str(len(springs_in_a_row)) <= max(schema) else min(schema)
#         for spring_group in possibility
#         for springs_in_a_row in filter(lambda it: it, spring_group.split('0'))
#     ]

#     return output


# @functools.cache
# def gen_combo(unknowns, unknown_combos, i):
#     ret_list = []
#     if i < unknown_combos:
#         ret_list.extend(gen_combo(unknowns, unknown_combos, i+1))

#     ret_list.append(bin(i)[2:].zfill(unknowns))
#     return ret_list
#     # return [bin(combo)[2:].zfill(unknowns) for combo in range(unknown_combos)]

# with open('condition.txt', 'r') as file:
#     count = 0
#     for nbr, line in enumerate(file.read().splitlines()):
#         springs, _, schema = line.partition(' ')
#         schema = schema.split(',')
        
#         ext_springs = ''
#         for i in itertools.repeat(springs, 5):
#             ext_springs += i + '?'
#         springs = ext_springs[:-1]

#         ext_schema = []
#         for i in itertools.repeat(schema, 5):
#             ext_schema.extend(i)
#         schema = ext_schema

#         spring_groups = filter(lambda it: it, springs.split('.'))
#         list_of_combos = []
#         for group in spring_groups:
#             unknowns = len(group.replace('#', ''))
#             unknown_combos = 2 ** unknowns

#             combos = gen_combo(unknowns, unknown_combos, 0)  # [bin(combo)[2:].zfill(unknowns) for combo in range(unknown_combos)]
#             for i, char in enumerate(group):
#                 if char == '#':
#                     combos = list(map(lambda el: el[:i] + '1' + el[i:], combos))

#             list_of_combos.append(combos)

#         list_of_combos = list(map(lambda el: list(set(parse(el, schema))), list_of_combos))

#         possibilities = filter(
#             lambda it: it == schema,
#             itertools.product(*list_of_combos)
#         )

#         for _ in possibilities:
#             count += 1

#         print('31')
#         # count += len(list(possibilities))
#         # for i, possibility in enumerate(possibilities):
#         #     print(i)
#         #     if parse(possibility) == schema:
#         #         count += 1
#         # break
#     print(count)
