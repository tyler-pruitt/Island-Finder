# island-operations
## `IslandFinder()`
### Finds contiguous regions (or "islands") in a matrix where all values in the island are greater than a threshold

A function which finds contiguous regions (or "islands") in a matrix where 
all values in the island are greater than a threshold 
(but not necessarily the same). The function takes a threshold, 
a minimum island size, and an arbitrarily sized matrix as inputs. 
The function outputs a matrix (same size as the input matrix) 
of booleans. It does not wrap around matrix edges. Corner neighbors are 
not sufficient for island continuity. For example, if the the inputs 
are: threshold = 5, min island size = 3, and matrix is

```
[4 4 4 2 2]
[4 2 2 2 2]
[2 2 8 7 2]
[2 8 8 8 2]
[8 2 2 2 8]
```

Then the output would be

```
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 1 1 0]
[0 1 1 1 0]
[0 0 0 0 0]
```

## `IslandCluster()`
### Clusters and counts the contiguous regions (or "islands") in a binary matrix (of 0s and 1s)

For example, if the matrix is

```
[0 0 0 0 0]
[0 1 1 0 0]
[0 1 1 0 0]
[0 1 0 0 1]
[0 0 0 1 1]
```

Then the output will be

```
[0 0 0 0 0]
[0 1 0 0 0]
[0 0 0 0 0]
[0 0 0 0 1]
[0 0 0 0 0]
```

and the island count will be 2
