---
layout: post
title: 54 - Spiral Matrix
date: 2015-11-14 19:20:05.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.**


``` java
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<Integer>();
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

``` python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ret = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while True:
            for j in range(left, right + 1):
                ret.append(matrix[top][j])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for j in reversed(range(left, right + 1)):
                ret.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break
            for i in reversed(range(top, bottom + 1)):
                ret.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ret
```
