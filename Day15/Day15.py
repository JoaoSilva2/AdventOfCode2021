import sys
import math
from queue import PriorityQueue

class PriorityEntry():
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority
    def get_data(self):
        return self.data
    def __lt__(self, other):
        return self.priority < other.priority
    


def get_adjacent(origin, dimension):
    adj = []
    x,y = origin
    for pos in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < dimension and pos[1] < dimension:
            adj.append(pos)
    return adj


def least_cost_past(cave_map, dimension):
    queue = PriorityQueue()
    distances = {}
    visited = {}
    for y in range(dimension):
        for x in range(dimension):
            if x == y == 0:
                distances[(x,y)] = 0
            else:
                distances[(x,y)] = math.inf
    queue.put(PriorityEntry(distances[(0,0)], (0,0)))
    while not queue.empty():
        current = queue.get().get_data()
        if current == (dimension-1,dimension-1):
            return distances[(dimension-1,dimension-1)]
        visited[current] = 1
        for adj in get_adjacent(current, dimension):
            if adj in visited.keys():
                continue
            new_dist = distances[current] + int(cave_map[adj[1]][adj[0]])

            if new_dist < distances[adj]:
                distances[adj] = new_dist
                queue.put(PriorityEntry(distances[adj], adj))
                
        del distances[current]
        
if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    cave_map = [list(line.replace("\n","")) for line in file.readlines()]
    dimension = len(cave_map)
    print(least_cost_past(cave_map, dimension))

    increased_cave = []
    for j in range(5):
        for line in cave_map:
            new_line = []
            for i in range(5):
                for value in line:
                    new_value = int(value) + i + j
                    if new_value >= 10:
                        new_value = new_value - 10 + 1
                    new_line.append(new_value)
            increased_cave.append(new_line)
    print(least_cost_past(increased_cave, dimension*5))
