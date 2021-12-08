#this solution is horrible but I don't want to optimize it 
def parse_digits(signals, outputs):
    signals = [set(signal.strip()) for signal in signals.split()]
    outputs = [''.join(sorted(set(output.strip()))) for output in outputs.split()]

    mapping = {}
    for signal in signals:
        if len(signal) == 2:
            one = signal
            mapping[''.join(sorted(signal))] = 1
        elif len(signal) == 4:
            four = signal
            mapping[''.join(sorted(signal))] = 4
        elif len(signal) == 3:
            seven = signal
            mapping[''.join(sorted(signal))] = 7
        elif len(signal) == 7:
            eight = signal
            mapping[''.join(sorted(signal))] = 8

    for signal in signals:
        if signal == one or signal == four or signal == seven or signal == eight:
            continue
        if (len(signal.intersection(one)) == 1 and
        len(signal.intersection(four)) == 2 and
        len(signal.intersection(seven)) == 2):
            mapping[''.join(sorted(signal))] = 2
        elif (len(signal.intersection(one)) == 2 and
        len(signal.intersection(four)) == 3 and
        len(signal.intersection(seven)) == 3 and
        len(signal) == 5):
            mapping[''.join(sorted(signal))] = 3
        elif (len(signal.intersection(one)) == 1 and
        len(signal.intersection(four)) == 3 and
        len(signal.intersection(seven)) == 2 and
        len(signal) == 5):
            mapping[''.join(sorted(signal))] = 5
        elif (len(signal.intersection(one)) == 1 and
        len(signal.intersection(four)) == 3 and
        len(signal.intersection(seven)) == 2 and
        len(signal) == 6):
            mapping[''.join(sorted(signal))] = 6
        elif (len(signal.intersection(one)) == 2 and
        len(signal.intersection(four)) == 4 and
        len(signal.intersection(seven)) == 3):
            mapping[''.join(sorted(signal))] = 9
        elif (len(signal.intersection(one)) == 2 and
        len(signal.intersection(four)) == 3 and
        len(signal.intersection(seven)) == 3):
            mapping[''.join(sorted(signal))] = 0
    try:
        print(mapping)
        digits = int(''.join([str(mapping[output]) for output in outputs]))
    except Exception as e:
        print(mapping)
        print(e)

    return digits

def parse_line(line):
    inputs, outputs = line.split(' | ')
    digits = parse_digits(inputs, outputs)
    #print(digits)
    return digits



with open('data/input.txt', 'r') as f:
    data = [parse_line(line) for line in f.readlines()]

def solution(data):
    print(data)
    return sum(data)
    #unique_digit_length = len([digit for output in data for digit in output if digit in (1,4,7,8)])
    #return unique_digit_length

print(solution(data))
