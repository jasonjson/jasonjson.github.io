---
layout: post
title: Rotate Image
date: 2015-10-21 14:34:51.000000000 -04:00
tags:
- Algorithm
categories:
- Matrix
author: Jason
---
<p><strong><em>You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).</em></strong></p>


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
