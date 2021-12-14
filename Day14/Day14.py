import sys

def parse_input(file):
    polymer = file.readline().replace("\n", "")
    rules = dict(map(lambda s: s.split(" -> "), file.read().split("\n")[1:-1]))
    return polymer, rules

def add_new_pair(pairs, pair, count):
    try:
        pairs[pair] += count
    except:
        pairs[pair] = count

def find_polymer_formula(polymer, rules, steps):
    pairs = {}
    char_counter = dict((rules[key], polymer.count(rules[key])) for key in rules.keys())

    for i in range(len(polymer)-1):
        try:
            pairs[polymer[i]+polymer[i+1]] += 1
        except:
            pairs[polymer[i]+polymer[i+1]] = 1
    for step in range(steps):
        keys = [key for key in pairs.keys() if pairs[key] != 0]
        copy = dict(pairs)
        for pair in keys:
            result = rules[pair]
            count = copy[pair]
            char_counter[result] += count
            add_new_pair(pairs, pair[0]+result, count)
            add_new_pair(pairs, result+pair[1], count)
            pairs[pair] -= count

    return max(char_counter.values()) - min(char_counter.values())

if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    polymer, rules = parse_input(file)
    print("Part1: ", find_polymer_formula(polymer, rules, 40))
    #print("Part2: ", find_polymer_formula(polymer, rules, 40))
