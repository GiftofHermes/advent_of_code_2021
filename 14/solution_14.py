from collections import Counter
from copy import deepcopy

def parse_line(line):
    k,v = line.split(' -> ')
    return {k: f'{k[0]}{v}{k[1]}'}

def parse_line2(line):
    k,v = line.split(' -> ')
    return {k: v}

def create_pairs(polymer):
    return map(lambda x: ''.join(x), zip(polymer[:-1], polymer[1:]))

def create_pairs2(polymer):
    return Counter(zip(polymer[:-1], polymer[1:]))


def join_pairs(pairs, rules):
    pairs = [rules.get(pair, pair) for pair in pairs]
    polymer = ''
    for pair in pairs[:-1]:
        polymer += pair[:-1]
    polymer += pairs[-1]
    return polymer

def step(polymer, rules):
    pairs = create_pairs(polymer)
    polymer = join_pairs(pairs, rules)
    return polymer

def create_mapping(rules):
    return {(k[0], k[1]): [(k[0],v), (v,k[1])] for k, v in rules.items()}

def step2(pairs, mapping):
    pairs_copy = deepcopy(pairs)
    for pair in pairs:
        if new := mapping.get(pair, None):
            pairs_copy[new[0]] += pairs[pair]
            pairs_copy[new[1]] += pairs[pair]
            pairs_copy[pair] -= pairs[pair]
            if pairs_copy[pair] <= 0:
                del pairs_copy[pair]
    return pairs_copy

def create_letter_counter_for_solution2(pairs):
    counter = Counter()
    for pair, value in pairs.items():
        #counter[pair[0]] += value
        counter[pair[1]] += value
    return counter

def solution1():
    with open('data/input.txt', 'r') as f:
        polymer = f.readline().strip()
        f.readline()
        rules = [parse_line(line.strip()) for line in f.readlines()]
        rules = {k:v for rule in rules for k,v in rule.items()}
    n_step = 10
    for i in range(n_step):
        polymer = step(polymer, rules)

    counter = Counter(polymer)
    most_common = counter.most_common()[0]
    least_common = counter.most_common()[-1]

    print(most_common)
    print(least_common)
    return print(most_common[1] - least_common[1])


def solution2():
    with open('data/input.txt', 'r') as f:
        polymer = f.readline().strip()
        f.readline()
        rules = [parse_line2(line.strip()) for line in f.readlines()]
        rules = {k:v for rule in rules for k,v in rule.items()}

    n_step = 40
    pairs = create_pairs2(polymer)
    mapping = create_mapping(rules)
    for i in range(n_step):
        pairs = step2(pairs, mapping)
    counter = create_letter_counter_for_solution2(pairs)
    most_common = counter.most_common()[0]
    least_common = counter.most_common()[-1]
    print(pairs)
    print(most_common)
    print(least_common)
    return most_common[1]-least_common[1]

print(solution1())
print(solution2())
