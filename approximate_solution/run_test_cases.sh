#!/usr/bin/env bash

small=($(ls test_cases/small))
medium=($(ls test_cases/medium))
large=($(ls test_cases/large))

time=3000
interval=100

for item in ${small[@]}
do
  printf "small/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < test_cases/small/$item
  printf "\n"
done

for item in ${medium[@]}
do
  printf "medium/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < test_cases/medium/$item
  printf "\n"
done

for item in ${large[@]}
do
  printf "large/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < test_cases/large/$item
  printf "\n"
done
