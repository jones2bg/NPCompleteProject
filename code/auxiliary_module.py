# Author(s): Blake Jones
# Description: This module serves as a helper for our project.
# Date: 4/25/22

import random

# method to generate our complete cycles, given n vertices.
def complete_cycle_graph(vertices):

    # create our dictionary component.
    graph = {}
    # we will use the storing convention
    # {int: [(int, int)]} which is {vertex: [(connecting vertex, weight)]}

    # loop through each vertex and connect it to every other vertex.
    for i in range(vertices):
        # initialize the adjacency list
        graph[i] = []
        for j in range(vertices):
            # statement to ensure the node cannot be connected to itself
            if i != j:
                weight = random.randint(1,100)
                connecting_set = (j, weight)
                graph[i].append(connecting_set)

    return graph
            

def main():
    print(complete_cycle_graph(15))

if __name__ == "__main__":
    main()