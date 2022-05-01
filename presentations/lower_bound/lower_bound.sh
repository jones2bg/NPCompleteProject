# using the python3 lower_bound.py < ../../approximate_solution/test_cases/small/3_node.txt
# works and this doesn't for some reason
small=($(ls ../../approximate_solution/test_cases/small))
medium=($(ls ../../approximate_solution/test_cases/medium))
large=($(ls ../../approximate_solution/test_cases/large))

for item in ${small[@]}
do
    ./lower_bound.py < ../../approximate_solution/test_cases/small/$item
done

for item in ${medium[@]}
do
    ./lower_bound.py < ../../approximate_solution/test_cases/medium/$item
done

for item in ${small[@]}
do
    ./lower_bound.py < ../../approximate_solution/test_cases/large/$item
done