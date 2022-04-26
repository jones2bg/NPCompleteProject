#!/usr/bin/env python3

# Author(s): Blake Jones
# Description: This script creates an approximation of the TSP problem.
# Date: 4/26/22

import random
import time

def approximate(start_node, runtime, graph, edges):
    print(start_node)
    print(runtime)
    print(graph)
    print(edges)

def main():
    timeout = int(input())
    start_node = int(input())

    v, e = [int(x) for x in input().split(' ')[:2]]
    edges = [[int(x) for x in input().split(' ')] for _ in range(0, e)]

    graph = dict()
    weights = dict()

    for i in range(0, v):
        graph[i] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]

    approximate(timeout, 0, graph, edges)

if __name__ == "__main__":
    main()