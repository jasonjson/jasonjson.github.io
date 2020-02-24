---
layout: post
title: 74 - Search a 2D Matrix
date: 2015-10-21 02:28:30.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.**

``` python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        lo, hi = 0, len(matrix) * len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            i, j = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
```
