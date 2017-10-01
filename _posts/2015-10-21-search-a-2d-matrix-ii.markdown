---
layout: post
title: Search a 2D Matrix II
date: 2015-10-21 02:31:22.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
- Sorting
author: Jason
---
<p><strong><em>Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it. This matrix has the following properties:</p>

Integers in each row are sorted from left to right.</p>
Integers in each column are sorted from up to bottom.</p>
No duplicate integers in each row or column.</em></strong></p>
``` java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        // write your code here
        int count = 0;
        if (matrix == null || matrix.length == 0) return count;
        if (matrix[0] == null || matrix[0].length == 0) return count;
        //error check
        int row = matrix.length, col = matrix[0].length;
        int i = 0, j = col - 1, count = 0;
        while (i < row && j >= 0) {
            if (matrix[i][j] == target) {
                count ++;
                j--;//bug: forget to decrement j, j is the smallest element in this column, the rest elements woule be larger
            } else if (matrix[i][j] > target) {
                j--;
            } else {
                i++;
            }
        }
        return count;
    }
}
```
