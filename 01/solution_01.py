with open('data/input.txt') as f:
    data =[int(line) for line in f.readlines()]

def find_increasing_in_a_list(data):
    sum(map(lambda x: 0 > (x[0] - x[1]), zip(data[0:-1], data[1:])))

result1 = find_increasing_in_a_list(data)

windowed = list(map(lambda x: sum(x), zip(data[0:-2], data[1:-1], data[2:])))
result2 = find_increasing_in_a_list(windowed)
print(result2)
