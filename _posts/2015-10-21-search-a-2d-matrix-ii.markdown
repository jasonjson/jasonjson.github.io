---
layout: post
title: 240 - Search a 2D Matrix II
date: 2015-10-21 02:31:22.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:**
* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.


``` java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) return False;
        int row = matrix.length, col = matrix[0].length;
        int i = 0, j = col - 1;
        while (i < row && j >= 0) {
            if (matrix[i][j] == target) {
                return True
            } else if (matrix[i][j] > target) {
                j--;
            } else {
                i++;
            }
        }
        return False;
    }
}
```

``` python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
```
