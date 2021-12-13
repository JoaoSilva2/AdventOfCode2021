import sys
finished = 0

class TreeNode:
    def __init__(self, id, start=None) -> None:
        self.children = []
        self.visited = []
        if start != None:
            self.visited.append(start)
        self.id = id
    
    def add_children(self, node):
        self.children.append(node)
    
    def add_visited(self, node):
        self.visited += node.get_visited()
        if all([char.islower() for char in self.id]):
            self.visited.append(self.id)
    
    def get_id(self):
        return self.id
    
    def get_visited(self):
        return self.visited

def BuildGraph(lines):
    graph = {}
    for line in lines:
        vertice_a, vertice_b = line.split("-")
        vertice_b = vertice_b.replace("\n", "")
        try:
            graph[vertice_a].append(vertice_b)
        except:
            graph[vertice_a] = [vertice_b]
            
        try:
            graph[vertice_b].append(vertice_a)
        except:
            graph[vertice_b] = [vertice_a]

    return graph

def Recursion(node, graph, extra=None):
    global finished
    if node.get_id() == "end":
        finished += 1
        return

    for adj in graph[node.get_id()]:
        if adj not in node.get_visited() or (adj == extra and node.get_visited().count(extra) < 2):
            new_node = TreeNode(adj)
            node.add_children(new_node)
            new_node.add_visited(node)
            Recursion(new_node, graph, extra)

if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    #--------------------------Build Graph--------------------------------------
    graph = BuildGraph(lines)
    #--------------------------Create Tree--------------------------------------
    root = TreeNode("start", "start")
    #--------------------------Part one-----------------------------------------
    Recursion(root, graph)
    part_1 = finished
    #--------------------------Part two-----------------------------------------
    for key in graph.keys():
        root = TreeNode("start", "start")
        if key not in ("start", "end") and all([char.islower() for char in key]):
            Recursion(root, graph, key)
            finished -= part_1

    print("Part 1: {}".format(part_1))
    print("Part 2: {}".format(finished))
    file.close()
