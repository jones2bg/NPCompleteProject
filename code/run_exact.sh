#!/usr/bin/env bash

small=($(ls small))
medium=($(ls medium))
large=($(ls large))

cpus=$(nproc)

for item in ${small[@]}
do
  printf "small/$item\n"
  time ./exact_TSP.py < small/$item
  printf "\n"
done

for item in ${medium[@]}
do
  printf "medium/$item\n"
  time ./exact_TSP.py < medium/$item
  printf "\n"
done

for item in ${large[@]}
do
  printf "large/$item\n"
  time ./exact_TSP.py < large/$item
  printf "\n"
done
