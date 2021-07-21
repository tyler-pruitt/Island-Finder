#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:11:54 2020
Last modified on Tue Jul 20 23:02:43 2021
Author: Tyler Pruitt
"""

import numpy as np
import random

def searchUpper(answer, isSearched, count, rows, columns, n, r, i, j):
    """
    Searches above previous matrix position by decreasing n by 1
    """
    if i+n != 0: #if not an upper edge
        if answer[i-1+n][j+r] == 1 and isSearched[i-1+n][j+r] == False: #if upper is 1 and not seached before
            count += 1
            isSearched[i-1+n][j+r] = True #record that position has been counted before for this i, j pair
            count = searchUpper(answer, isSearched, count, rows, columns, n-1, r, i, j) #feed count back into branches
            count = searchLeft(answer, isSearched, count, rows, columns, n-1, r, i, j)
            count = searchRight(answer, isSearched, count, rows, columns, n-1, r, i, j)
    return count

def searchLower(answer, isSearched, count, rows, columns, n, r, i, j):
    """
    Searches below previous matrix position by increasing n by 1
    """
    if i+n != rows - 1: #if not a lower edge
        if answer[i+1+n][j+r] == 1 and isSearched[i+1+n][j+r] == False: #if lower is 1 and not searched before
            count += 1
            isSearched[i+1+n][j+r] = True #record that position has been counted before for this i, j pair
            count = searchLower(answer, isSearched, count, rows, columns, n+1, r, i, j) #feed count back into branches
            count = searchLeft(answer, isSearched, count, rows, columns, n+1, r, i, j)
            count = searchRight(answer, isSearched, count, rows, columns, n+1, r, i, j)
    return count

def searchLeft(answer, isSearched, count, rows, columns, n, r, i, j):
    """
    Searches to the left of previous matrix position by decreasing r by 1
    """
    if j+r != 0: #if not a left edge
        if answer[i+n][j-1+r] == 1 and isSearched[i+n][j-1+r] == False: #if left is 1 and not searched before
            count += 1
            isSearched[i+n][j-1+r] = True #record that position has been counted before for this i, j pair
            count = searchUpper(answer, isSearched, count, rows, columns, n, r-1, i, j) #feed count back into branches
            count = searchLower(answer, isSearched, count, rows, columns, n, r-1, i, j)
            count = searchLeft(answer, isSearched, count, rows, columns, n, r-1, i, j)
    return count

def searchRight(answer, isSearched, count, rows, columns, n, r, i, j):
    """
    Searches to the right of previous matrix position by increasing r by 1
    """
    if j+r != columns - 1: #if not an edge
        if answer[i+n][j+1+r] == 1 and isSearched[i+n][j+1+r] == False: #if right is 1 and not searched before
            count += 1
            isSearched[i+n][j+1+r] = True #record that position has been counted before for this i, j pair
            count = searchUpper(answer, isSearched, count, rows, columns, n, r+1, i, j) #feed count back into branches
            count = searchLower(answer, isSearched, count, rows, columns, n, r+1, i, j)
            count = searchRight(answer, isSearched, count, rows, columns, n, r+1, i, j)
    return count

def islandFinder(matrix, threshold, minIslandSize):
    """
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
    by 1's and everything else represented by 0's
    """
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    result = np.zeros( (rows, columns), dtype=int) #create a same sized matrix as input matrix of zeros
    
    for i in range(rows): #loop inserts 1's where values are greater than threshold
        for j in range(columns):
            if matrix[i][j] > threshold:
                result[i][j] = 1
    
    for i in range(rows): #loop removes 1's which do not satisfy min island size requirements without wrapping edges
        for j in range(columns):
            
            if result[i][j] == 1: #looking at 1's now
                record = np.zeros( (rows, columns), dtype=bool) #set up record of if position has been searched before
                
                #initializing variables for looking up and down (n) and looking left and right (r) for each i,j pair
                n, r = 0, 0
                
                count = 1 #count i,j position (must count single island first)
                record[i][j] = True #record that position has been counted
                count = searchUpper(result, record, count, rows, columns, n, r, i, j) #branch out through upper neighbors to i,j position and retrieve count
                count = searchLower(result, record, count, rows, columns, n, r, i, j) #feed count back into other branches as previous branch is exhausted
                count = searchLeft(result, record, count, rows, columns, n, r, i, j)
                count = searchRight(result, record, count, rows, columns, n, r, i, j)
                
                if count < minIslandSize:
                    result[i][j] = 0
    return result

def islandCluster(matrix, clusterSize=1, isRandom=False):
    """
    Counts the number of contiguous regions (or "islands") or clusters in a matrix.
    Clusters together or shrinks clusters to the size of the element.
    At the moment, maxIslandSize does nothing since it would affect islandCount and the clustering of other originally separate islands.

    Parameters
    ----------
    matrix : np.array or any other matrix
        A matrix of contiguous regions (or "islands") where all values in the island 
    are greater than a threshold (but not necessarily the same). Island elements are represented by 1, non-island elements are represented by 0.
    clusterSize : int, optional
        The number of elements set to represent the island after clustering. If number of elements is less than maxIslandSize, it will be the number of elements in the island. The default is 1.
    isRandom : bool, optional
        If set to True, a random element in the island is chosen to represent the island, instead of the top left most element. The default is False.

    Returns
    -------
    result : np.array
        A matrix of clustered islands with every island represented by at least one element.
    islandCount : int
        The number of contiguous regions (or "islands") in a matrix.
    """
    
    """
    if clusterSize < 1 or clusterSize > count:
        raise ValueError
    """
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    result = np.zeros( (rows, columns), dtype=int)
    
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix[i][j]
    
    for i in range(rows):
        for j in range(columns):
            if result[i][j] != 0:
                record = np.zeros( (rows, columns), dtype=bool)
                
                #initializing variables for looking up and down (n) and looking left and right (r) for each i,j pair
                n, r = 0, 0
                
                count = 1 #count i,j position (must count single island first)
                record[i][j] = True #record that position has been counted
                count = searchUpper(result, record, count, rows, columns, n, r, i, j) #branch out through upper neighbors to i,j position and retrieve count
                count = searchLower(result, record, count, rows, columns, n, r, i, j) #feed count back into other branches as previous branch is exhausted
                count = searchLeft(result, record, count, rows, columns, n, r, i, j)
                count = searchRight(result, record, count, rows, columns, n, r, i, j)
                
                if isRandom:
                    randRow = random.randrange(len(record))
                    randCol = random.randrange(len(record[randRow]))
                    
                    while record[randRow][randCol] == False:
                        randRow = random.randrange(len(record))
                        randCol = random.randrange(len(record[randRow]))
                    
                    for m in range(rows):
                        for n in range(columns):
                            if record[m][n] == True and (m != randRow or n != randCol):
                                result[m][n] = 0
                                record[m][n] = False
                else:
                    for m in range(rows):
                        for n in range(columns):
                            if record[m][n] == True and (m != i or n != j):
                                result[m][n] = 0
                                record[m][n] = False
    
    islandCount = 0
    
    for i in range(rows):
        for j in range(columns):
            if result[i][j] != 0:
                islandCount += 1
    
    return result, islandCount

def islandCounter(matrix):
    """
    Counts the number of "islands" or clusters in a matrix.
    Assumes that the clusters are separated.
    """
    rows = len(matrix)
    columns = len(matrix[0])
    
    count = 0
    
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != 0:
                count += 1
    
    return count

