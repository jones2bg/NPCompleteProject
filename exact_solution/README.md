# Exact Solution

## Running All Test Cases
Run run_test_cases.sh with no arguments to run all provided test cases.

```
./run_test_cases.sh
```

## Running Individually
Run exact_TSP.py and provide an input graph and a selected starting node on stdin.

```
./exact_TSP.py < test_cases/small/3_node.txt
```

## Expected Output
The test cases run are included in expected_output.txt.

For each test case, the output format is:
```
the test being run
the minimum cost for that test
the path chosen
and the runtime in hour:minute:second format
```

## Example of Correctness
As a test of correctness, I ran small/4_node.txt by hand.

```
4 12
0 1 31
0 2 92
0 3 17
1 0 31
1 2 57
1 3 71
2 0 92
2 1 57
2 3 75
3 0 17
3 1 71
3 2 75
0
```

This is a graph with 4 vertices and 12 edges, with starting vertex 0.

I have enumerated the possible paths and added their cost as follows:
```
0 1 2 3 0: 31 + 57 + 75 + 17 = 180
0 2 1 3 0: 92 + 57 + 71 + 17 = 237
0 2 3 1 0: 92 + 75 + 71 + 31 = 269
0 1 3 2 0: 31 + 71 + 75 + 92 = 269
0 3 1 2 0: 17 + 71 + 57 + 92 = 237
0 3 2 1 0: 17 + 75 + 57 + 31 = 180
```

Clearly the lowest cost path here is either the first or last, adding to 180, and as expected, the output for this particular test case from `expected_output.txt` is:

```
small/4_node.txt
180
[0, 1, 2, 3, 0]
0:00:00.000013
```
