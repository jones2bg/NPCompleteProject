# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import math
from unicodedata import unidata_version
from connected_components import count_and_label

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
    min_cost = 0
    graph.pop(0)
    visited = []
    for u in graph.keys():
        for v in graph[u]:
            if (not (u,v) in visited or (v,u) in visited) and (u,v) in weights.keys():
                min_cost += weights[(u,v)]
                visited.append((u,v))
    
    print(min_cost)

#(V-1) * V /2 for a complete graph

def MST(V,E): #num of vert and all edges
    def AddAllSafeEdges(E,F,count, comp):
        safe = [None] * count
        for u,v in E:
            if comp[u] != comp[v]:
                if safe[comp[u]] == None or E[(u,v)] < safe[comp[u]][2]: 
                    safe[comp[u]] = (u,v,E[(u,v)]) 
                if safe[comp[v]] == None or E[(u,v)] < safe[comp[v]][2]:
                    safe[comp[v]] = (u,v,E[(u,v)])

            #print(safe)
        for u,v,w in safe:
                #F.append(e)
                #check if u / v in already in the list
            if(v not in F[u] and u not in F[v]):
                F[u].append(v)
                F[v].append(u)
        
        
    F = {}
    #F = dict.fromkeys(V,[])
    F = {k:[] for k in V}
    #print(F)
    count= count_and_label(F)[0]
    #labels = count_and_label(F)[1]
    while count > 1:
        AddAllSafeEdges(E,F,count,count_and_label(F)[1])
        count = count_and_label(F)[0]
    return F

    
if __name__ == "__main__":
    main()