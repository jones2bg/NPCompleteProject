#!/usr/bin/env bash

mkdir -p small
mkdir -p medium
mkdir -p large

sizes=(3 4 5 6 7 8 9 10 11 12 13 14)
weight_limits=(100 1000 5000)

for e in "${sizes[@]}"
do
  printf "$e\n${weight_limits[0]}" | ./generate_graph.py > small/"$e"_node.txt
  printf "$e\n${weight_limits[1]}" | ./generate_graph.py > medium/"$e"_node.txt
  printf "$e\n${weight_limits[2]}" | ./generate_graph.py > large/"$e"_node.txt
done
