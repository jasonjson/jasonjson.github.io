---
layout: post
title: Spiral Matrix II
date: 2015-11-14 19:28:04.000000000 -05:00
tags:
- Algorithm
categories:
- Matrix
author: Jason
---
**Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.**


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

``` python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        num = 1
        ret = [[0] * n for i in xrange(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while num <= n * n:
            for j in xrange(left, right + 1):
                ret[top][j] = num
                num += 1
            top += 1
            for i in xrange(top, bottom + 1):
                ret[i][right] = num
                num += 1
            right -= 1
            for j in reversed(xrange(left, right + 1)):
                ret[bottom][j] = num
                num += 1
            bottom -= 1
            for i in reversed(xrange(top, bottom + 1)):
                ret[i][left] = num
                num += 1
            left += 1
        return ret
```
