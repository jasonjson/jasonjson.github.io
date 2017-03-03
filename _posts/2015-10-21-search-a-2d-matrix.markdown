---
layout: post
title: Search a 2D Matrix
date: 2015-10-21 02:28:30.000000000 -04:00
tags: algorithm
categories:
- Binary Search Tree
- Matrix
author: Jason
---
<p><strong><em>Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.</em></strong></p>


``` java
public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) return false;
        if (matrix[0] == null || matrix[0].length == 0) return false;
        int row = matrix.length, col = matrix[0].length;
        int lo = 0, hi = row * col - 1;
        while (lo <= hi){
            int mid = (lo + hi) / 2;
            int number = matrix[mid/col][mid%col];
            if (number == target) {
                return true;
            }else if (number > target) {
                hi = mid - 1;
            }else {
                lo = mid + 1;
            }
        }
        return false;
    }
}
```
