# Implementation of the count-and-label 
# connected component counting algorithm.
#
# Author: John Bowers
# Version: Mar 17, 2021
# Version of the iterative dfs that takes as input
# a list of labels, one per vertex, and a starting 
# vertex v and uses iterative depth-first-search
# to label each vertex with a given currentLabel
# 
# Parameters: 
#   * graph is an adjaceny list or adjacency with vertex names 0-(n-1)
#   * v is the vertex to DFS from
#   * labels is an array of length V which is -1 if the vertex is unvisited
#   * currentLabel is the label to set on every visited vertex
#
# labels is an out-parameter and will be modified destructively during the 
# run of this operation. 
#
# March 2022 -- molloykp
#  Changed code to label components starting a 0 (instead of 1)
def dfs_label(graph, v, labels, currentLabel):
    bag = [v]
    while bag: # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = currentLabel
            for w in graph[u]:
                bag.append(w)
# Counts the number of connected components in the graph
# and labels each vertex with its connected component index
#
# Parameters:
#   * graph given as an adjaceny list/set structure with vertices 0..(n-1)
#
# Returns: 
#   count, labels
#   where count is the number of connected components in the graph
#   and labels is the labeling of each vertex's connected component
#   starting from index 1. 
def count_and_label(graph):
    labels = [-1 for _ in range(len(graph))] # Initially all labels are 0
    count = -1
    for v in range(len(graph)): # for each vertex
        if labels[v] == -1: # if v is not visited
            count += 1
            dfs_label(graph, v, labels, count)
    return count+1, labels
# A little main program to test on a graph with two components: 
if __name__ == "__main__":
    graph = [
        set([1]), # 0's neighbors 
        set([0, 2, 3]), # 1's neighbors
        set([1, 3]), # 2's neighbors
        set([1, 2]), # 3's neighbors
        set([5]), # 4's neighbors
        set([4]), # 5's neighbors
    ]
    count, labels = count_and_label(graph)
    print(f"Number of connected components: {count}")
    print(f"Vertex labels: {labels}")