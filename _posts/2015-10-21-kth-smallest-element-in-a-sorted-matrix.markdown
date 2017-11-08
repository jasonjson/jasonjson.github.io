---
layout: post
title: 378 - Kth Smallest Element in a Sorted Matrix
date: 2015-10-21 14:23:52.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.**


``` python
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        if not matrix:
            return -1

        heap = [(matrix[0][j], 0, j) for j in xrange(len(matrix[0]))]
        while k > 1:
            curr, row, col = heapq.heappop(heap)
            if row + 1 < len(matrix):
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            k -= 1
        return heapq.heappop(heap)[0]
```
