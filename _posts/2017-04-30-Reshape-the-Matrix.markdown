---
layout: post
title: Reshape the Matrix
date: 2017-04-30
tags:
- Algorithm
categories:
- Matrix
author: Jason
---
**In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively. The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were. If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.**

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        #use () instead of [] to get a generator
        num_list = (x for y in nums for x in y)
        #put column number in a list first
        return [[num_list.next() for i in range(c)] for j in range(r)]
```
