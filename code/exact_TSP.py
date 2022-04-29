#!/usr/bin/env python3

"""
    name: Quade Curry
"""

import sys
import itertools
import datetime
import time

def tsp(graph, weights, start):
    # Create a set of all the vertices in the graph.
    vertices = set(graph)

    # Create a set of vertices that does not include the start node.
    other_vertices = vertices - set([start])

    # Generate every permutation of those vertices to get the traversals.
    traversals = itertools.permutations(other_vertices)

    min_cost = sys.maxsize
    min_traversal = None

    # Calculate the cost of every traversal.
    for traversal in traversals:
        # Start with the starting vertex.
        previous = start
        cost = 0
        # Add up the cost of every edge in the traversal.
        for vertex in traversal:
            cost += weights[(previous, vertex)]
            previous = vertex
        # Add the cost of the last vertex in the traversal back to the start.
        cost += weights[(previous, start)]

        if cost < min_cost:
            min_cost = cost
            min_traversal = list(traversal)
            min_traversal.insert(0, start)
            min_traversal.append(start)

    return min_cost, min_traversal

def main():
    v, e = [int(x) for x in input().split(' ')[:2]]
    edges = [[int(x) for x in input().split(' ')] for _ in range(0, e)]
    start = int(input())

    graph = dict()
    weights = dict()

    for i in range(0, v):
        graph[i] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]

    start_time = time.time()
    min_cost, min_traversal = tsp(graph, weights, start)
    end_time = time.time()

    print(min_cost)
    print(min_traversal)

    print(datetime.timedelta(seconds=end_time - start_time))

if __name__ == '__main__':
    main()
