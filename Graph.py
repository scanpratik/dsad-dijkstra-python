from collections import defaultdict
from Heap import Heap
import sys


def print_arr(dist, n):
    print("Vertex\tDistance from source")
    for i in range(n):
        print("%d\t\t%d" % (i, dist[i]))


def print_src_dest(dist, src, dest, parent, vertices_map):
    vertices_map_invert = {v: k for k, v in vertices_map.items()}
    # print("\nVertex \t\tDistance from Source\tPath")
    # print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, dest, dist[dest]), end="")
    # printPath(parent, dest)
    # print()
    # print("\n%s --> %s \t\t%d \t\t\t\t\t" % (vertices_map_invert[int(src)], vertices_map_invert[int(dest)], dist[dest]), end="")
    path_list = []
    printPathString(parent, dest, vertices_map_invert, path_list)
    print()
    print()
    print(f"Shortest route from the hospital '{vertices_map_invert[int(src)]}' to reach the airport '{vertices_map_invert[int(dest)]}' is {path_list} and it has minimum travel distance {dist[dest]}km")


# A utility function to print the constructed distance array
def printSolution(src, dist, parent):
    print("Vertex \t\tDistance from Source\tPath")
    for i in range(1, len(dist)):
        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]), end="")
        printPath(parent, i)


# Function to print shortest path from source to j using parent array
def printPath(parent, j):

    # Base Case : If j is source
    if parent[j] == -1:
        print(j, end=",")
        return
    printPath(parent, parent[j])
    print(j, end=",")


def printPathString(parent, j, vertices_map_invert, path_list):

    # Base Case : If j is source
    if parent[j] == -1:
        # print(vertices_map_invert[int(j)], end=",")
        path_list.append(vertices_map_invert[int(j)])
        return
    printPathString(parent, parent[j], vertices_map_invert, path_list)
    # print(vertices_map_invert[int(j)], end=",")
    path_list.append(vertices_map_invert[int(j)])


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.parent = [-1] * V

        # Adds an edge to an undirected graph

    def addEdge(self, src, dest, weight):

        # Add an edge from src to dest.  A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

        # The main function that calulates distances

    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src, dest, vertices_map):

        V = self.V  # Get the number of vertices in graph
        dist = []  # dist values used to pick minimum
        # weight edge in cut

        # minHeap represents set E
        minHeap = Heap()

        #  Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(V):
            dist.append(sys.maxsize)
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

            # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop, min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and pCrawl[1] + dist[u] < dist[v]:
                    dist[v] = pCrawl[1] + dist[u]
                    self.parent[v] = u

                    # update distance value
                    # in min heap also
                    minHeap.decreaseKey(v, dist[v])

        print_arr(dist, V)
        printSolution(src, dist, self.parent)
        print_src_dest(dist, src, dest, self.parent, vertices_map)
