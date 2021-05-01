from collections import defaultdict
import sys
r = range
max_weight = sys.maxsize


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

        self.graph = [[0] * self.vertices for _ in r(self.vertices)]
        self.visited = [0] * self.vertices  
        self.distances = [max_weight] * self.vertices

    # Add edge to graph start --> end point with specific weight!
    def add_edge(self, start, end, weight):
        self.graph[start][end] = weight

    def print_dist(self, dist):
        for _ in r(self.vertices):
            print("vert ", _, "\tdist ", self.distances[_])

    def dijkstra(self, end_point):
        self.distances[end_point] = 0

        for vert in r(self.vertices):

            # we need to check for minimum but not visited!!
            my_min, min_index = max_weight, 0
            for _ in r(self.vertices):
                if not self.visited[_]:
                    if my_min > self.distances[_]:
                        my_min = self.distances[_]
                        min_index = _

            # check the flag for visited
            self.visited[min_index] = 1

            # # iterate and update if needed
            for adj in r(self.vertices):
                # check for edge and visited
                val = self.graph[min_index][adj]
                if not self.visited[adj] and val != 0:
                    # check if needed update
                    if self.distances[adj] > self.distances[min_index] + val:
                        self.distances[adj] = self.distances[min_index] + val
        self.print_dist(self.distances)
