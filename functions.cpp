#include <iostream>
#include <string>
#include <vector>

using namespace std;

int search(string direction, std::vector<std::vector<int>> answer, std::vector<std::vector<bool>> &isSearched, int count, int rows, int columns, int n, int r, int i, int j);
std::vector<std::vector<int>> islandFinder(std::vector<std::vector<int>> matrix, int threshold, int minIslandSize);
std::vector<std::vector<int>> islandCluster(std::vector<std::vector<int>> matrix);
int islandCounter(std::vector<std::vector<int>> matrix);

int search(string direction, std::vector<std::vector<int>> answer, std::vector<std::vector<bool>> &isSearched, int count, int rows, int columns, int n, int r, int i, int j) {    
    // Searches in the direction in relation to the matrix position i, j

    int a, b, x, y;
    string steps[3];

    if (direction == "up") {
        a = i + n;
        b = 0;
        x = n - 1;
        y = r;
        
        steps[0] = "up";
        steps[1] = "left";
        steps[2] = "right";
    } else if (direction == "down") {
        a = i + n;
        b = rows - 1;
        x = n + 1;
        y = r;
        
        steps[0] = "down";
        steps[1] = "left";
        steps[2] = "right";
    } else if (direction == "left") {
        a = j + r;
        b = 0;
        x = n;
        y = r - 1;
        
        steps[0] = "up";
        steps[1] = "down";
        steps[2] = "left";
    } else if (direction == "right") {
        a = j + r;
        b = columns - 1;
        x = n;
        y = r + 1;
        
        steps[0] = "up";
        steps[1] = "down";
        steps[2] = "right";
    } else {
        cout << "Direction not specified correctly in function call for 'search'. Encountered incorrect entry for direction of '" << direction << "'," << endl;
    }
    
    if (a != b) {
        // If not an upper edge
        if (answer[i+x][j+y] == 1 && isSearched[i+x][j+y] == false) {
            // If upper is 1 and not searched before
            count++;
            
            // Record that position has been counted before for this i, j pair
            isSearched[i+x][j+y] = true;

            // Feed count back into branches
            for (string path : steps) {
                count = search(path, answer, isSearched, count, rows, columns, x, y, i, j);
            }
        }
    }

    return count;
}

std::vector<std::vector<int>> islandFinder(std::vector<std::vector<int>> matrix, int threshold, int minIslandSize) {
    /*
    Finds contiguous regions (or "islands") in a matrix where all values in the island 
    are greater than a threshold (but not necessarily the same).
    */
    
    int rows, columns;
    rows = matrix.size();
    columns = matrix[0].size();

    // Create a same sized matrix as input matrix of zeros

    std::vector<std::vector<int>> result(rows, std::vector<int> (columns));

    for (int i=0;i<rows;i++) {
        for (int j=0;j<columns;j++) {
            if (matrix[i][j] > threshold) {
                // Insert 1's where values are greater than threshold
                result[i][j] = 1;
            } else {
                result[i][j] = 0;
            }
        }
    }

    // Removes 1's which do not satisfy min island size requirements without wrapping edges
    for (int i=0;i<rows;i++) {
        for (int j=0;j<columns;j++) {
            // Looking at only 1's now
            if (result[i][j] == 1) {

                // Set up record of if position has been searched before
                std::vector<std::vector<bool>> record(rows, std::vector<bool> (columns));

                for (int x=0;x<rows;x++) {
                    for (int y=0;y<columns;y++) {
                        record[x][y] = false;
                    }
                }

                // Initialize variables for looking up and down (n) and looking left and right (r) for each i,j pair
                int n(0), r(0);

                // Count i,j position (must count single island first)
                int count = 1;

                // Record that position has been counted
                record[i][j] = true;

                // Branch out through upper neighbors to i,j position and retrieve count
                // Feed count back into other branches as previous branch is exhausted
                count = search("up", result, record, count, rows, columns, n, r, i, j);
                count = search("down", result, record, count, rows, columns, n, r, i, j);
                count = search("left", result, record, count, rows, columns, n, r, i, j);
                count = search("right", result, record, count, rows, columns, n, r, i, j);

                if (count < minIslandSize) {
                    result[i][j] = 0;
                }
            }
        }
    }

    return result;
}

std::vector<std::vector<int>> islandCluster(std::vector<std::vector<int>> matrix) {
    int rows, columns;
    rows = matrix.size();
    columns = matrix[0].size();

    // Create a same sized matrix as input matrix of zeros

    std::vector<std::vector<int>> result(rows, std::vector<int> (columns));

    for (int i=0;i<rows;i++) {
        for (int j=0;j<columns;j++) {
            result[i][j] = matrix[i][j];
        }
    }

    // Removes 1's which do not satisfy min island size requirements without wrapping edges
    for (int i=0;i<rows;i++) {
        for (int j=0;j<columns;j++) {
            // Looking at only 1's now
            if (result[i][j] != 0) {

                // Set up record of if position has been searched before
                std::vector<std::vector<bool>> record(rows, std::vector<bool> (columns));

                for (int x=0;x<rows;x++) {
                    for (int y=0;y<columns;y++) {
                        record[x][y] = false;
                    }
                }

                // Initialize variables for looking up and down (n) and looking left and right (r) for each i,j pair
                int n(0), r(0);

                // Count i,j position (must count single island first)
                int count = 1;

                // Record that position has been counted
                record[i][j] = true;

                // Branch out through upper neighbors to i,j position and retrieve count
                // Feed count back into other branches as previous branch is exhausted
                count = search("up", result, record, count, rows, columns, n, r, i, j);
                count = search("down", result, record, count, rows, columns, n, r, i, j);
                count = search("left", result, record, count, rows, columns, n, r, i, j);
                count = search("right", result, record, count, rows, columns, n, r, i, j);

                for (int x=0;x<rows;x++) {
                    for (int y=0;y<columns;y++) {
                        if (record[x][y] == true && (x != i || y != j)) {
                            result[x][y] = 0;
                            record[x][y] = false;
                        }
                    }
                }
            }
        }
    }

    return result;
}

int islandCounter(std::vector<std::vector<int>> matrix) {
    // Counts the number of "islands" or clusters in a matrix.
    // Assumes that the clusters are separated.

    int count = 0;

    for (int i=0;i<matrix.size();i++) {
        for (int j=0;j<matrix[0].size();j++) {
            if (matrix[i][j] != 0) {
                count++;
            }
        }
    }

    return count;
}
