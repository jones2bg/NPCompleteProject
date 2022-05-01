#!/usr/bin/env bash

small=($(ls test_cases/small))
medium=($(ls test_cases/medium))
large=($(ls test_cases/large))

for item in ${small[@]}
do
  printf "small/$item\n"
  ./exact_TSP.py < test_cases/small/$item
  printf "\n"
done

for item in ${medium[@]}
do
  printf "medium/$item\n"
  ./exact_TSP.py < test_cases/medium/$item
  printf "\n"
done

for item in ${large[@]}
do
  printf "large/$item\n"
  ./exact_TSP.py < test_cases/large/$item
  printf "\n"
done
