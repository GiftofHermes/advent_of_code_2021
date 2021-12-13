with open('data/input.txt', 'r') as f:
    dots = []
    folds = []
    for line in f.readlines():
        line = line.strip()
        if line[:4] == 'fold':
            axis, index = line[11:].split('=')
            folds.append((axis, int(index)))
        elif line == '':
            continue
        else:
            x, y = list(map(int, line.split(',')))
            dots.append([x,y])

def fold(dots, axis, index):
    axis = 0 if axis == 'x' else 1
    result = []
    for dot in dots:
        if dot[axis] < index:
            result.append(dot)
        elif dot[axis] == index:
            continue
        if dot[axis] > index:
            dot[axis] = index+index-dot[axis]
            result.append(dot)
    return result

def non_overlapping_dots(dots):
    return set(map(tuple, dots))

def draw(dots):
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    map = []
    for i in range(max_y+1):
        row = []
        for j in range(max_x+1):
            row.append(0)
        map.append(row)

    for dot in dots:
        x = dot[0]
        y = dot[1]
        map[y][x] = 1
    print(map)
    res = ''
    for row in map:
        for num in row:
            if num == 1:
                res += '#'
            else:
                res += '.'
        res += '\n'
    print(res)


print(dots)
print(folds)

for instruction in folds:
    axis = instruction[0]
    index = instruction[1]
    dots = fold(dots, axis, index)

print(non_overlapping_dots(dots))
draw(dots)

print(len(non_overlapping_dots(dots)))
