# island-finder
Write a function, in the programming language of your choice, 
which finds contiguous regions (or "islands") in a matrix where 
all values in the island are greater than a threshold 
(but not necessarily the same). The function should take a threshold, 
a minimum island size, and an arbitrarily sized matrix as inputs. 
The function should output a matrix (same size as the input matrix) 
of booleans. Do not wrap around matrix edges. Corner neighbors are 
not sufficient for island continuity. For example, if the the inputs 
are: threshold = 5, min island size = 3, and matrix is

[4 4 4 2 2]\
[4 2 2 2 2]\
[2 2 8 7 2]\
[2 8 8 8 2]\
[8 2 2 2 8]


Then the output would be

[0 0 0 0 0]\
[0 0 0 0 0]\
[0 0 1 1 0]\
[0 1 1 1 0]\
[0 0 0 0 0]]
