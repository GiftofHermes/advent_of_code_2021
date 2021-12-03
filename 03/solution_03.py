from enum import Enum, auto

class Kind(Enum):
    OXYGEN = auto()
    CO2 = auto()

def bits_to_decimal(bits):
    return int(''.join(map(lambda x: str(x), bits)), 2)

def find_most_common(data):
    data = sorted(data)
    index = int((len(data) - 1) / 2) if len(data) % 2 == 1 else int((len(data)/2))
    return int(data[index])

with open('data/input.txt') as f:
    data =[line.strip() for line in f.readlines()]

def solution1(data):
    def find_gamma_and_epsilon(data):
        data = zip(*data)
        gamma_bits, epsilon_bits = zip(*[(bit := find_most_common(bits), 1-bit) for bits in data])

        gamma = bits_to_decimal(gamma_bits)
        epsilon = bits_to_decimal(epsilon_bits)
        return gamma, epsilon


    gamma, epsilon = find_gamma_and_epsilon(data)
    power_consumption = gamma * epsilon
    return power_consumption
print(solution1(data))

def solution2(data):
    def find_oxygen_and_CO2(data):
        oxygen_data = data[:]
        CO2_data = data[:]
        def filter_bits(data, kind):
            for i in range(len(data[0])):
                index_bits = list(zip(*data))[i]

                most_common = find_most_common(index_bits)
                least_common = 1-most_common
                if kind == Kind.OXYGEN:
                    filter_bit = most_common
                elif kind == Kind.CO2:
                    filter_bit = least_common
                data = list(filter(lambda x: x[i] == str(filter_bit), data))
                if len(data) == 1:
                    return data[0]

        oxygen_bits = filter_bits(oxygen_data, Kind.OXYGEN)
        CO2_bits = filter_bits(CO2_data, Kind.CO2)

        oxygen = bits_to_decimal(oxygen_bits)
        CO2 = bits_to_decimal(CO2_bits)

        return oxygen, CO2
    oxygen, CO2 = find_oxygen_and_CO2(data)

    life_support_rating = oxygen * CO2
    return life_support_rating

print(solution2(data))
