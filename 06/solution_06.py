from collections import Counter

with open('data/input.txt', 'r') as f:
    data = list(map(int, f.readline().strip().split(',')))

def solution1(data, n_step):
    def tick(data):
        for i, item in enumerate(data):
            if item != 0:
                item -= 1
            else:
                item = 6
                data.append(9)
            data[i] = item

    for i in range(n_step):
        tick(data)
        #print(i+1, '-', data)

    return len(data)


# a way more efficient solution than the first one
def solution2(data, n_step):
    def tick(fish_counts):
        num_0 = fish_counts[0]
        #print(num_0)
        for i in range(len(fish_counts)-1):
            fish_counts[i] = fish_counts[i+1]
        fish_counts[6] += num_0
        fish_counts[8] = num_0
        #print(fish_counts)

    counter = Counter(data)
    data #= #counter
    fish_counts = [0] * 9
    for k,v in counter.items():
        fish_counts[k] = v

    for i in range(n_step):
        tick(fish_counts)
    return sum(fish_counts)

n_step = 256
#print(solution1(data, n_step))
print(solution2(data, n_step))
