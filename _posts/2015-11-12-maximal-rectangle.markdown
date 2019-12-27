---
layout: post
title: 85 - Maximal Rectangle
date: 2015-11-12 18:23:08.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.**


``` java
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;

        int row = matrix.length, col = matrix[0].length, max = 0;
        int[] left = new int[col], right = new int[col], height = new int[col];
        Arrays.fill(right, col);//!!fill the right array

        for (int i = 0; i < row; i++) {
            int curr_left = 0, curr_right = col - 1;
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    height[j] ++;
                } else {
                    height[j] = 0;
                }
            }

            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    left[j] = Math.max(left[j], curr_left);
                } else {
                    left[j] = 0;
                    curr_left = j + 1;
                }
            }

            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    right[j] = Math.min(right[j], curr_right);
                } else {
                    right[j] = col - 1;
                    curr_right = j - 1;
                }
            }

            for (int j = 0; j < col; j++) {
                max = Math.max(max, height[j] * (right[j] - left[j] + 1));
            }
        }
        return max;
    }
}
```

``` python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #left[i]: the index of leftmost '1' in the current group
        #right[i]: the index of rightmost '1' plus one in the current group
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        height = [0] * col
        left = [0] * col
        right = [col] * col

        ret = 0
        for i in range(row):
            curr_left, curr_right = 0, col
            for j in range(col):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_left = j + 1
            for j in reversed(range(col)):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = col
                    curr_right = j
            for j in range(col):
                ret = max(ret, (right[j] - left[j]) * height[j])
        return ret
```
