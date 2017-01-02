---
layout: post
title: Spiral Matrix
date: 2015-11-14 19:20:05.000000000 -05:00
categories:
- Brain teaser
- Matrix
author: Jason
---
<p><strong><em>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.</em></strong></p>

``` java
public class Solution {
    public List<integer> spiralOrder(int[][] matrix) {
        List<integer> result = new ArrayList<integer>();
        if (matrix == null || matrix.length == 0) return result;
        
        int up = 0, down = matrix.length - 1, left = 0, right = matrix[0].length - 1;
        while (true) {
            for (int j = left; j <= right; j++) {
                result.add(matrix[up][j]);//print top row
            }
            up ++;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int i = up; i <= down; i++) {
                result.add(matrix[i][right]);//print right col
            }
            right--;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int j = right; j >= left; j--) {
                result.add(matrix[down][j]);//print bottom row
            }
            down --;
            if (crossBoundary(up, down, left, right)) {
                break;
            }            
            for (int i = down; i >= up; i--) {
                result.add(matrix[i][left]);//print left col
            }
            left ++;
            if (crossBoundary(up, down, left, right)) {
                break;
            }
        }
        return result;
    }    
    public boolean crossBoundary(int up, int down, int left, int right) {
        return up > down || left > right;
    }
}
```
