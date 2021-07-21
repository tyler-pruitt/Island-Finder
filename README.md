# island-operations
## `islandFinder(matrix, threshold, minIslandSize)`
### Finds contiguous regions (or "islands") in a matrix where all values in the island are greater than a threshold (but not necessarily the same)

```
Finds contiguous regions (or "islands") in a matrix where all values in the island 
are greater than a threshold (but not necessarily the same).

Parameters
----------
threshold : matrix elements must be greater than this value to be a part of
    an island
minIslandSize : minimum number of connecting (either top, bottom, left or right)
    island elements to constitute an island
matrix : np.array or other input matrix of arbitrary size

Returns
-------
result : matrix of same size as input matrix of booleans with islands represented
    by 1's and everything else represented by 0's; does not wrap around matrix edges;
    corner neighbors are not sufficient for island continuity
```

For example, if the the inputs 
are: threshold = 5, min island size = 3, and matrix is

```
[4 4 4 2 2]
[4 2 2 2 2]
[2 2 8 7 2]
[2 8 8 8 2]
[8 2 2 2 8]
```

then the output would be

```
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 1 1 0]
[0 1 1 1 0]
[0 0 0 0 0]
```

## `islandCluster(matrix, clusterSize=1, isRandom=False)`
### Clusters and counts the contiguous regions (or "islands") in a binary matrix (of 0s and 1s)

```
Counts the number of contiguous regions (or "islands") or clusters in a matrix.
Clusters together or shrinks clusters to the size of the element.
At the moment, maxIslandSize does nothing since it would affect islandCount and the clustering of other originally separate islands.

Parameters
----------
matrix : np.array or any other matrix
    A matrix of contiguous regions (or "islands") where all values in the island 
    are greater than a threshold (but not necessarily the same). Island elements are represented by 1, non-island elements are represented by 0.
clusterSize : int, optional
    The number of elements set to represent the island after clustering. If number of elements is less than maxIslandSize, it will be the number of elements in the     island. The default is 1.
isRandom : bool, optional
    If set to True, a random element in the island is chosen to represent the island, instead of the top left most element. The default is False.

Returns
-------
result : np.array
    A matrix of clustered islands with every island represented by at least one element.
islandCount : int
    The number of contiguous regions (or "islands") in a matrix.
```

For example, if the matrix is

```
[0 0 0 0 0]
[0 1 1 0 0]
[0 1 1 0 0]
[0 1 0 0 1]
[0 0 0 1 1]
```

then the output will be

```
[0 0 0 0 0]
[0 1 0 0 0]
[0 0 0 0 0]
[0 0 0 0 1]
[0 0 0 0 0]
```

and the island count will be `2`


## `islandCounter(matrix)`
### Counts the number of "islands" or clusters in a matrix.

```
Counts the number of "islands" or clusters in a matrix.
Assumes that the clusters are separated. The matrix need not be binary or of booleans.
```

For example, if the matrix is

```
[0 0 0 1 0]
[0 1 0 0 0]
[0 0 0 1 0]
[0 0 0 0 1]
[0 1 0 1 0]
```

then the island count will be `6`
