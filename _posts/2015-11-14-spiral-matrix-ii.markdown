---
layout: post
title: Spiral Matrix II
date: 2015-11-14 19:28:04.000000000 -05:00
categories:
- Binary Search Tree
- Matrix
author: Jason
---
<p><strong><em>Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.</em></strong></p>


``` java
public class Solution {
    public int[][] generateMatrix(int n) {
       int number = 1;
       int up = 0, down = n - 1, left = 0, right = n - 1;
       int[][] matrix = new int[n][n];
       while (number <= n * n) {
           for (int j = left; j <= right; j++) {
               matrix[up][j] = number ++;
           }
           up ++;
           for (int i = up; i <= down; i++) {
               matrix[i][right] = number ++;
           }
           right--;
           for (int j = right; j >= left; j--) {
               matrix[down][j] = number ++;
           }
           down --;
           for (int i = down; i >= up; i--) {
               matrix[i][left] = number ++;
           }
           left ++;
       }//while loop stops when we use up all numbers
       return matrix;
    }
}
```
