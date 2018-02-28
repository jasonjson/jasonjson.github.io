---
layout: post
title: 766 - Toeplitz Matrix
date: 2018-02-28
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element. Now given an M x N matrix, return True if and only if the matrix is Toeplitz.**


```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return False

        for i in xrange(len(matrix) - 1):
            for j in xrange(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
```
