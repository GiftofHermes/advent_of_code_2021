with open('data/input.txt') as f:
    data =[line.strip().split(' ') for line in f.readlines()]
    data = list(map(lambda x: (x[0], int(x[1])), data))

def find_horizontal_and_depth_solution1(data):
    horizontal = 0
    depth = 0
    for row in data:
        if row[0] == 'forward':
            horizontal += row[1]
        elif row[0] == 'down':
            depth += row[1]
        elif row[0] == 'up':
            depth -= row[1]
            depth = max(0, depth)
    return horizontal *  depth

def find_horizontal_and_depth_solution2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for row in data:
        if row[0] == 'forward':
            horizontal += row[1]
            depth += row[1] * aim
            depth = max(0, depth)
        elif row[0] == 'down':
            aim += row[1]
        elif row[0] == 'up':
            aim -= row[1]
            aim = max(0, aim)
    return horizontal *  depth


print(find_horizontal_and_depth_solution2(data))
