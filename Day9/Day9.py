import sys
import functools as ft

def BFS(floor_map, start):
    queue = [start]
    visited = [start]
    basin_size = 1
    while(queue != []):
        current = queue.pop(0)
        x,y = current
        adj = [adj_pos for adj_pos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if adj_pos in floor_map.keys()]
        for adj_pos in adj:
            if adj_pos not in visited and floor_map[adj_pos] != 9:
                queue.append(adj_pos)
                visited.append(adj_pos)
                basin_size += 1
    return basin_size


def find_low_points(lines):
    floor_map = {}
    y = 0
    for line in lines:
        x = 0
        for number in line[0:-1]:
            floor_map[(x, y)] = int(number)
            x += 1
        y += 1
    
    basin_sizes = []
    low_points_depth = 0
    for pos in floor_map.keys():
        if floor_map[pos] == 9:
            continue
        else:
            x, y = pos
            adj = [floor_map[pos] < floor_map[adj_pos] for adj_pos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if adj_pos in floor_map.keys()]
            if all(adj):
                basin_sizes.append(BFS(floor_map, pos))
                low_points_depth += floor_map[pos] + 1

    while(len(basin_sizes) != 3):
        basin_sizes.remove(min(basin_sizes))

    return (low_points_depth, ft.reduce(lambda x,y: x*y, basin_sizes))

if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    result = find_low_points(lines)
    print("Part1: ", result[0])
    print("Part2: ", result[1])
    file.close()
