#!/usr/bin/env python3

# Example code to read in a weighted graph output by the generator.

def main():
    v, e = [int(x) for x in input().split(' ')[:2]]
    edges = [[int(x) for x in input().split(' ')] for _ in range(0, e)]

    graph = dict()
    weights = dict()

    for i in range(0, v):
        graph[i] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]

    print(graph)
    print(weights)

if __name__ == '__main__':
    main()
