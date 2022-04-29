#!/usr/bin/env bash

small=($(ls small))
medium=($(ls medium))
large=($(ls large))

time=3000
interval=100

for item in ${small[@]}
do
  printf "small/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < small/$item
  printf "\n"
done

for item in ${medium[@]}
do
  printf "medium/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < medium/$item
  printf "\n"
done

for item in ${large[@]}
do
  printf "large/$item\n"
  printf "time/$time\n"
  ./approximate_TSP.py $time $interval < large/$item
  printf "\n"
done
