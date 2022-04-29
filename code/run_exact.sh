#!/usr/bin/env bash

small=($(ls small))
medium=($(ls medium))
large=($(ls large))

for item in ${small[@]}
do
  printf "small/$item\n"
  ./exact_TSP.py < small/$item
  printf "\n"
done

for item in ${medium[@]}
do
  printf "medium/$item\n"
  ./exact_TSP.py < medium/$item
  printf "\n"
done

for item in ${large[@]}
do
  printf "large/$item\n"
  ./exact_TSP.py < large/$item
  printf "\n"
done
