import sys

class Octopus:
    def __init__(self, energy) -> None:
        self.energy = energy
        self.flashed = False
    
    def get_energy(self):
        return self.energy
    
    def charge(self):
        if not self.flashed:
            self.energy += 1
    
    def flash(self):
        if self.energy > 9 and not self.flashed:
            self.flashed = True
    
    def charged_up(self):
        return self.energy > 9 and not self.flashed
    
    def reset(self):
        if self.flashed:
            self.energy = 0
            self.flashed = False

def print_map(width, height, octo_map):
    for y in range(height):
        for x in range(width):
            print(octo_map[(x,y)].get_energy(), end="")
        print("")

def all_flashing(octo_map):
    return all([octo_map[key].get_energy() == 0 for key in octo_map.keys()])

def count_flashes(lines):
    octo_map = {}
    num_flashes = 0

    width = 0
    height = 0

    y = 0
    for line in lines:
        line = line.replace("\n", "")
        x = 0
        for value in line:
            octo_map[(x,y)] = Octopus(int(value))
            x += 1
        width = x
        y += 1
    
    height = y

    step = 0
    while not all_flashing(octo_map):
        for key in octo_map.keys():
            octo_map[key].charge()
        
        to_flash = []
        for key in octo_map.keys():
            if octo_map[key].charged_up():
                to_flash.append(key)
        while to_flash:
            x, y = to_flash.pop(0)
            octo_map[(x,y)].flash()
            num_flashes += 1
            for adj_key in ((x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)):
                if adj_key in octo_map:
                    octo_map[adj_key].charge()
                    if octo_map[adj_key].charged_up() and adj_key not in to_flash:
                        to_flash.append(adj_key)
        
        for key in octo_map.keys():
            octo_map[key].reset()
        step += 1
    print(step)



if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    count_flashes(lines)
    file.close()
