from collections import Counter

def check_horizontal_or_vertical(x1,y1,x2,y2):
    return True if x1 == x2 or y1 == y2 else False

def parse_line(line, solution2):
    line = list(map(lambda x: list(map(int, x.split(','))), line.split(' -> ')))
    (x1, y1), (x2, y2) = line
    if check_horizontal_or_vertical(x1,y1,x2,y2):
        if x1 == x2:
            if y1 > y2:
                big_y = y1
                small_y = y2
            else:
                big_y = y2
                small_y = y1
            return [(x1, small_y+i) for i in range(big_y-small_y+1)]
        elif y1 == y2:
            if x1 > x2:
                big_x = x1
                small_x = x2
            else:
                big_x = x2
                small_x = x1
            return [(small_x+i, y1) for i in range(big_x-small_x+1)]
    elif solution2: # diagonal
        if y1 > y2:
            sign_y = -1
        else:
            sign_y = 1
        if x1 > x2:
            sign_x = -1
            sign_y *=-1
        else:
            sign_x = 1
        return [(x1+i, y1+i*sign_y) for i in range(0,x2-x1+1*sign_x, sign_x)]
    return []
data = []
with open('data/input.txt') as f:
    for line in f.readlines():
        data.extend(parse_line(line, solution2=True))


counter = Counter(data)
over_2 = [k for k, v in counter.items() if v>=2]

print(len(over_2))
#print(counter > 2)
