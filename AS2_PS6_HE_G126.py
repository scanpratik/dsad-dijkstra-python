"""
References
- https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/
- https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
- https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/
- https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/

"""
import sys
from Graph import Graph

vertices = set()
vertices_map = {}
counter = 0
edges = []
hospital = sys.maxsize
airport = sys.maxsize


def create_mapping(vertex):
    global counter
    vertices.add(vertex)
    vertices_map[vertex] = counter
    counter = counter + 1


def read_input_file(path):
    global hospital
    global airport

    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.isspace():
            continue
        if line.strip().startswith("Hospital"):
            _, hosp_node = line.strip().split(":")
            hospital = vertices_map[hosp_node.strip()]
        elif line.strip().startswith("Airport"):
            _, airport_node = line.strip().split(":")
            airport = vertices_map[airport_node.strip()]
        else:
            src, dest, w = line.strip().split("/")
            src, dest, w = src.strip(), dest.strip(), w.strip()

            if src not in vertices:
                create_mapping(src)
            if dest not in vertices:
                create_mapping(dest)

            edges.append((vertices_map[src], vertices_map[dest], w))


read_input_file("inputPS6.txt")

print(edges)
print(vertices_map)
print(vertices)
print(hospital)
print(airport)

"""
0 - a, 1 - b, 2 - c, 3 - d, 4 - e, 5 - f, 6 - g, 7 - h, 8 - i

a / b / 4
a / h / 8
b / c / 8
b / h / 11
c / d / 7
c / i / 2
c / f / 4
d / e / 9
d / f / 14
e / f / 10
f / g / 2
g / h / 1
g / i / 6
h / i / 7

"""

graph = Graph(len(vertices))

for src, dest, w in edges:
    graph.addEdge(int(src), int(dest), int(w))

graph.dijkstra(int(hospital), int(airport), vertices_map)


# graph.addEdge(0, 1, 4)
# graph.addEdge(0, 7, 8)
# graph.addEdge(1, 2, 8)
# graph.addEdge(1, 7, 11)
# graph.addEdge(2, 3, 7)
# graph.addEdge(2, 8, 2)
# graph.addEdge(2, 5, 4)
# graph.addEdge(3, 4, 9)
# graph.addEdge(3, 5, 14)
# graph.addEdge(4, 5, 10)
# graph.addEdge(5, 6, 2)
# graph.addEdge(6, 7, 1)
# graph.addEdge(6, 8, 6)
# graph.addEdge(7, 8, 7)
# graph.dijkstra(0)