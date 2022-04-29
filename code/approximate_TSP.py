#!/usr/bin/env python3

# Author(s): Blake Jones
# Description: This script creates an approximation of the TSP problem.
# Date: 4/26/22

import random
import time
import sys


def approximate(start_node, runtime, graph, nodes):
    # hold our current start time. 
    start_time = time.time()

    # generate a random path from the nodes
    path = list(nodes[start_node])
    no_start_end_path = list(nodes[start_node])
    # shuffle the nodes
    random.shuffle(path)
    # add the start to the front and end of the path.
    path.insert(0, start_node)
    path.append(start_node)
    
    curr_min = sys.maxsize
    # amount of paths taken.
    counter = 1
    
    # run our approximation for (runtime) seconds
    while time.time() < start_time + (runtime / 1000):
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[(path[i], path[i+1])]
        if cost < curr_min:
            curr_min = cost
            print("New Minimum Cost Path:")
            print(path)
            print("New Minimum Cost:", curr_min)
            print("Cumulative Amount of Paths Evaluated:", counter)
            print("")
        
        # sample two random items in the list.
        choices = random.sample(no_start_end_path, 2)
        index_first_ele = path.index(choices[0])
        index_second_ele = path.index(choices[1])
        
        # create the new path
        path[index_first_ele], path[index_second_ele] = path[index_second_ele], path[index_first_ele]
        counter += 1

# prompt for input and approximate the minima.
def main():
    runtime = int(input("runtime (milliseconds): "))    
    print("input graph: ")

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
    
    approximate(start_node, runtime, graph, nodes)

if __name__ == "__main__":
    main()
