#Doesn't work for the second solution.
# it finds a smaller cost than the answer. 
# I thought the problem could be algorithm only going right or down instead searching for a path using any cardinal direction
# but if that was the problem my cost can't be lower than the real answer. Right now it is so I don't know what the problem is. 
import copy

with open('data/input.txt', 'r') as f:
    lines = list(map(lambda x: [int(num) for num in x] , [line.strip() for line in f.readlines()]))
    cost = lines

def minCost(cost, row, col):

    # For 1st column
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]

    # For 1st row
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]

    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += (min(cost[i - 1][j],
                               cost[i][j - 1]))

    # Returning the value in
    # last cell
    return cost[row - 1][col - 1]


def calculate_risk(cost):

    row = len(cost)
    col = len(cost)
    cost[0][0] = 0
    return minCost(cost, row, col)

def calculate_full_risk(cost):
    def complete_cost_map(cost):

        base_cost = copy.deepcopy(cost)

        for i in range(1,5):
            for j, row in enumerate(base_cost):
                extension = []
                for col in row:
                    value = ( (col+i) % 9)
                    extension.append(value  if value > 0 else 9)
                cost[j].extend(extension)

        base_cost = copy.deepcopy(cost)
        for i in range(1,5):
            for j, row in enumerate(base_cost):
                extension = []
                for col in row:
                    value = ( (col+i) % 9)
                    extension.append(value  if value > 0 else 9)
                cost.append(extension)
        return cost

    cost = complete_cost_map(cost)

    row = len(cost)
    col = len(cost[0])
    print(row, col)
    return minCost(cost, row, col) - cost[0][0]

print(calculate_full_risk(cost))
