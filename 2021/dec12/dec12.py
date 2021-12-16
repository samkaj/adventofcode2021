from collections import deque

def main():
    # get input
    with open("input.txt") as f:
        paths = [line.strip().split('-') for line in f.readlines()]

    g = Graph()
    for path in paths:
        g.add(Edge(path[0], path[1]))
        g.add(Edge(path[1], path[0]))
    
    g.DFS('start', 'end')
    print(g.path_no)
    

class PQEntry:
    def __init__(self, node, bp, cost):
        self.node = node
        self.bp = bp
        self.cost = cost
        

class Edge:
    def __init__(self, to, fr):
        self.to = to
        self.fr = fr

    
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.n_edges = 0
        self.path_no = 0


    def add(self, edge: Edge) -> None:
        if not self.adjacency_list.get(edge.fr):
            self.adjacency_list[edge.fr] = []
        self.adjacency_list.get(edge.fr).append(edge)
        self.n_edges += 1


    def outgoing_edges(self, node: str) -> list:
        if not self.adjacency_list.get(node):
            return []
        return self.adjacency_list.get(node)
    

    def print_graph(self) -> None:
        for v in self.adjacency_list.keys():
            edges = self.outgoing_edges(v)
            if not edges:
                continue
            print([str(e) for e in edges])

    
    def DFS(self, start, goal):
        visited = {key :  False for key in self.adjacency_list.keys()}
        path = []
        self.recursiveDFS(start, goal, visited, path)

    def recursiveDFS(self, start, goal, visited: dict, path: list) -> list:
        if start.islower():
            visited[start] = True
        path.append(start)

        if start == goal:
            self.path_no += 1
        else:
            for edge in self.outgoing_edges(start):
                if not visited[edge.to]:
                    self.recursiveDFS(edge.to, goal, visited, path)

        path.pop()
        visited[start] = False
                

    def get_path(self, entry: PQEntry) -> list:
        path = []
        while entry.bp:
            path.append(entry.node)
            entry = entry.bp
        path.append(entry.node)
        path.reverse()
        return path

if __name__ == "__main__":
    main()
