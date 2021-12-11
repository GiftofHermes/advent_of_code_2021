

def parse_line(line):
    return [int(num) for num in line]

def pretty_print(data):
    res = ''
    for row in data:
        res += ''.join([str(num) for num in row]) + '\n'
    print(res)

def get_valid_directions(i,j, n=10):
    valid_directions = []
    max_index = n-1
    if i != 0:
        valid_directions.append([i-1, j])
    if j != 0:
        valid_directions.append([i, j-1])
    if i!= 0 and j != 0:
        valid_directions.append([i-1, j-1])
    if i!= max_index:
        valid_directions.append([i+1, j])
    if j != max_index:
        valid_directions.append([i, j+1])
    if i!= max_index and j != max_index:
        valid_directions.append([i+1, j+1])
    if i!= max_index and j != 0:
        valid_directions.append([i+1, j-1])
    if i!= 0 and j != max_index:
        valid_directions.append([i-1, j+1])
    return valid_directions


def step(data):
    def pulse_nines(over_nine, pulsed, data):
        for (i, j) in over_nine:
            for di, dj in get_valid_directions(i,j):
                if [di, dj] not in pulsed:
                    data[di][dj] += 1
        return data

    over_nine = []
    for i, row in enumerate(data):
        for j, num in enumerate(row):
            data[i][j] += 1
            if data[i][j] > 9:
                over_nine.append([i,j])

    data = pulse_nines(over_nine, list(),data)
    after_pulse_over_nine = [(i, j) for i, row in enumerate(data) for j, num in enumerate(row) if num > 9]
    while len(over_nine) - len(after_pulse_over_nine) != 0:
        to_pulse = list(set(after_pulse_over_nine) - set((i,j) for i,j in over_nine))
        pulse_nines(to_pulse, over_nine, data)
        over_nine.extend(to_pulse)
        after_pulse_over_nine = [(i, j) for i, row in enumerate(data) for j, num in enumerate(row) if num > 9]
    for i, j in over_nine:
        data[i][j] = 0
    return data, len(over_nine)


#10 x 10
with open('data/input.txt', 'r') as f:
    data = [parse_line(line.strip()) for line in f.readlines()]

def solution1(data):
    pretty_print(data)
    pulsed = 0
    n_steps = 100
    for i in range(n_steps):
        data, n = step(data)
        pulsed += n
        pretty_print(data)
    print(pulsed)

def solution2(data):
    i = 0
    while sum(num for row in data for num in row) != 0:
        step(data)
        i+= 1
    return i
i = solution2(data)
print(i)
