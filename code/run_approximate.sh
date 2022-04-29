#!/usr/bin/env bash

small=($(ls small))
medium=($(ls medium))
large=($(ls large))

times_=(1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000)

for time in ${times_[@]}
  do
  for item in ${small[@]}
  do
    printf "small/$item\n"
    printf "time/$time\n"
    ./approximate_TSP.py $time < small/$item
    printf "\n"
  done
done

for time in ${times_[@]}
  do
  for item in ${medium[@]}
  do
    printf "medium/$item\n"
    time ./approximate_TSP.py $time < medium/$item
    printf "\n"
  done
done

for time in ${times_[@]}
  do
  for item in ${large[@]}
  do
    printf "large/$item\n"
    time ./approximate_TSP.py $time < large/$item
    printf "\n"
  done
done