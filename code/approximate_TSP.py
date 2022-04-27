#!/usr/bin/env python3

# Author(s): Blake Jones
# Description: This script creates an approximation of the TSP problem.
# Date: 4/26/22

import random
import time


def approximate(start_node, runtime, graph):
    # hold our current start time.
    start_time = time.time()

    # generate a random path from the nodes
    path = list(graph.keys())
    path.remove(start_node)
    random.shuffle(path)
    path.insert(0, start_node)
    path.append(start_node)

    # run our approximation for (runtime) seconds
    while time.time() < start_time + runtime:
        pass
        


# prompt for input and approximate the minima.
def main():
    start_node = int(input("start node (int): "))
    runtime = int(input("runtime (seconds): "))    
    print("input graph: ")

    v, e = [int(x) for x in input().split(' ')[:2]]
    edges = [[int(x) for x in input().split(' ')] for _ in range(0, e)]

    graph = dict()

    for i in range(v):
        graph[i] = []

    for edge in edges:
         graph[edge[0]].append((edge[1], edge[2]))
   
    approximate(start_node, runtime, graph)

if __name__ == "__main__":
    main()