#!/usr/bin/env python3

# Author(s): Blake Jones
# Description: This script creates an approximation of the TSP problem using a random approach.
# Date: 4/26/22

import random
import time
import sys


def approximate(start_node, runtime, interval, graph, nodes):
    start_time = time.time()

    # Generate a random path from the nodes.
    path = list(nodes[start_node])
    no_start_end_path = list(nodes[start_node])

    # Shuffle the nodes.
    random.shuffle(path)

    # Add the start to the front and end of the path.
    path.insert(0, start_node)
    path.append(start_node)

    min_path = []
    curr_min = sys.maxsize
    # Amount of paths taken.
    counter = 1

    next_interval = time.time() + (interval / 1000)
    current_interval = interval

    # Run our approximation for (runtime) seconds.
    while time.time() < start_time + (runtime / 1000):
        if (time.time() > next_interval):
            print("Runtime:", current_interval)
            print("Minimum Cost Path:")
            print(min_path)
            print("Minimum Cost:", curr_min)
            print("Paths evaluated:", counter)
            print()
            next_interval = time.time() + (interval / 1000)
            current_interval += interval

        cost = 0
        for i in range(len(path) - 1):
            cost += graph[(path[i], path[i+1])]
        if cost < curr_min:
            curr_min = cost
            min_path = path.copy()

        # sample two random items in the list.
        choices = random.sample(no_start_end_path, 2)
        index_first_ele = path.index(choices[0])
        index_second_ele = path.index(choices[1])

        # create the new path
        path[index_first_ele], path[index_second_ele] = path[index_second_ele], path[index_first_ele]
        counter += 1

    print("Runtime:", current_interval)
    print("Minimum Cost Path:")
    print(min_path)
    print("Minimum Cost:", curr_min)
    print("Paths evaluated:", counter)

def main():
    # Amount of time to run in miliseconds
    runtime = int(sys.argv[1])
    # Interval to print minimum path found.
    interval = int(sys.argv[2])

    v, e = [int(x) for x in input().split(' ')[:2]]
    edges = [[int(x) for x in input().split(' ')] for _ in range(0, e)]
    start_node = int(input())

    graph = dict()
    nodes = dict()

    for i in range(v):
        nodes[i] = set()

    for edge in edges:
        nodes[edge[0]].add(edge[1])
        graph[(edge[0], edge[1])] = edge[2]

    approximate(start_node, runtime, interval, graph, nodes)

if __name__ == "__main__":
    main()
