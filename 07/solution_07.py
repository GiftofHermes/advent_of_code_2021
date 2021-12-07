with open('data/input.txt') as f:
    data = [int(num) for num in f.readline().split(',')]

def solution(data, kind):
    max_data = max(data)
    min_data = min(data)

    best_fuel = 9999999999
    for i in range(min_data, max_data+1):
        if kind == 1:
            fuel = sum([abs(num-i) for num in data])
        else:
            fuel = sum([abs(num-i)*(abs(num-i)+1)/2 for num in data])
        if fuel < best_fuel:
            best_fuel = fuel
            best_i = i
    return best_fuel


print(solution(data, 1))
print(solution(data, 2))
