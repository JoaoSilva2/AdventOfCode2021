import sys
import math

def calculate_media(positions, float_media):
    lower = 0
    higher = 0
    for key in positions.keys():
        if key >= float_media:
            higher += positions[key]
        else:
            lower += positions[key]
    if lower > higher:
        return (math.floor(float_media), 1)

    return (math.ceil(float_media), -1)

def minimize_fuel(line):
    positions = {}
    least_fuel = num_values = total_sum = 0
    for value in line:
        if value not in positions.keys():
            positions[value] = 1
        else:
            positions[value] += 1
        total_sum += value
        num_values += 1

    previous_media = -1
    current_media = 0
    while(current_media != previous_media):
        previous_media = current_media
        current_media, aux = calculate_media(positions, total_sum/num_values)
        total_sum = 0
        keys = list(positions.keys())
        for key in keys:
            if key*aux > current_media*aux and current_media not in positions:
                positions[current_media] = positions[key]
                least_fuel += abs(current_media - key)*positions[key]
                del positions[key]
            elif key*aux > current_media*aux and current_media in positions:
                positions[current_media] += positions[key]
                least_fuel += abs(current_media - key)*positions[key]
                del positions[key]
        for key in positions.keys():
            total_sum += positions[key]*key
    for key in positions:
        least_fuel += abs(current_media - key)*positions[key]

    return least_fuel

def minimize_fuel_2(file_lines):
    max_value = max(file_lines)
    min_fuel = math.inf
    for value in range(0, max_value):
        aux = 0
        for position in file_lines:
            aux += abs(position-value)*(abs(position-value)+1)//2
        #hit parabole minimum
        if aux > min_fuel:
            break
        min_fuel = aux
    return min_fuel

if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    line = [int(value) for value in file.readline().split(",")]
    print("Part1: ", minimize_fuel(line))
    print("Part2: ", minimize_fuel_2(line))
    file.close()
