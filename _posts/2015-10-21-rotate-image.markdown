---
layout: post
title: 48 - Rotate Image
date: 2015-10-21 14:34:51.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).**


``` java
public class Solution {
    public void rotate(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int n = matrix.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];//前一个row等于后一个col，前一个col + 后一个row = n - 1
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = temp;
            }
        }
    }
}
```

``` python
#顺时针旋转,先将第一行最后一行互换,并向中间进行,然后沿对角线互换
# 逆时针旋转,先将左边与右边互换,然后沿对角线互换
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            for i in xrange(len(matrix)):
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]
            top += 1
            bottom -= 1

        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
