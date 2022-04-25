# Travelling Salesman Problem

## Problem Assignments
Problem Presentation: Ryan
Exact Solution Code: Quade
Approximation Presentation: Miguel
Appxorimation Code: Blake

## Input
Normal adjancency list with weights.

n vertices
weight vertex connected vertices

We will write a program to generate a text file in this format, it will take the number of vertices and a range of values that will be randomly selected from to assign a weight to each vertex.

## Bounds
### Lower Bound
A lower bound can be found by removing a vertex, then finding a minimum spanning tree: Use Prim’s or Kruskal’s algorithm to find the length of the minimum spanning tree. Add to this the lengths of the two shortest edges connected to the missing vertex. Since any Hamiltonian cycle with a vertex removed will necessarily be a spanning tree of the remaining vertices, it follows that its length will be at least as great as that of the minimum spanning tree of those vertices. And the most efficient way to connect this tree to the final vertex is via the two shortest e.

### Upper Bound
An upper bound can be found using the ‘Nearest Neighbour’ algorithm: Start at a particular vertex, and travel to the nearest unused vertex. Continue until all vertices are included, then return to the start vertex. This will always produce a valid Hamiltonian cycle, and therefore must be at least as long as the minimum cycle. Hence, it is an upper bound. By choosing different starting vertices, a number of different upper bounds can be found. The lower the upper bound, the better, as it gives us more information.
