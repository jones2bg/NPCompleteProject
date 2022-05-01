#!/usr/bin/env python3

# Author(s): Blake Jones, Quade Curry
# Description: This script generates a graph of n vertices with random edge weights.
# Date: 4/25/22

import random

# Generate a complete graph with n vertices named 0, vertices-1, with randomly
# distributed weights
def generate_graph(vertices, wrange):
    edges = {}

    # loop through each vertex and connect it to every other vertex.
    for v1 in range(vertices):
        for v2 in range(vertices):
            # ensure the node cannot be connected to itself
            if v1 != v2:
                # check if reverse edge already exists.
                if (v2, v1) in edges:
                    weight = edges[(v2, v1)]
                else:
                    weight = random.randint(1,wrange)

                edges[(v1, v2)] = weight

    return edges

def main():
    n = int(input())
    wrange = int(input())
    weights = generate_graph(n, wrange)

    print(n, len(weights))
    for w in weights:
        print(w[0], w[1], weights[w])

    print(random.randrange(n))

if __name__ == "__main__":
    main()
