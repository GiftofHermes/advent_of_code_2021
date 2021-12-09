
def parse_line(line):
    return [int(letter) for letter in line]

def positions_to_check(i,j,data):
    n_row = len(data)
    n_col = len(data[0])

    i, j-1
    i, j+1
    i-1, j
    i+1, j

    positions = []
    if i != 0:
        positions.append([i-1, j])
    if i != n_row-1:
        positions.append([i+1, j])
    if j != 0:
        positions.append([i, j-1])
    if j != n_col-1:
        positions.append([i, j+1])
    return positions

# could be way more efficient with graph and pruning
def find_lowest_points(data):
    lowest_points = []
    lowest_points_index = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            positions = positions_to_check(i,j,data)
            add_lowest_point = True
            for position in positions:
                if col >= data[position[0]][position[1]]:
                    add_lowest_point = False
            if add_lowest_point:
                lowest_points.append(col)
                lowest_points_index.append([i,j])
    return lowest_points, lowest_points_index

def calculate_risk(lowest_points):
    return sum([i+1 for i in lowest_points])

with open('data/input.txt') as f:
    data = [parse_line(line.strip()) for line in f.readlines()]

def find_basin(i,j, data):
    checked_positions = [[i,j]]
    queue = []
    def positions_to_add(i,j,x,y,data):
        if data[x][y] != 9 and data[x][y] > data[i][j]:
            return True
        else:
            return False

    positions = [position for position in positions_to_check(i,j,data)
                if positions_to_add(i,j,position[0], position[1], data)]
    queue.extend(positions)

    while queue:
        current = queue.pop()
        checked_positions.append(current)
        i, j = current
        positions = [position for position in positions_to_check(i,j,data)
                    if positions_to_add(i,j,position[0], position[1], data) and
                    position not in checked_positions]
        queue.extend(positions)
        
    return len(set(map(tuple,checked_positions)))

lowest_points, lowest_points_index = find_lowest_points(data)
#risk = calculate_risk(lowest_points)
#print(risk) # solution1
#print(find_basin(0,1,data))
basins = [find_basin(i,j, data) for i,j in lowest_points_index]

print(basins)
top_3 = sorted(basins, key=lambda x: -x)[:3]
print(top_3)
print(top_3[0] * top_3[1] * top_3[2] )
