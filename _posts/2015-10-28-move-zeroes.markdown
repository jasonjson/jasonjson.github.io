---
layout: post
title: 283 - Move Zeroes
date: 2015-10-28 13:19:18.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements. For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]. Note: You must do this in-place without making a copy of the array. Minimize the total number of operations.**

``` python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        zero_index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1
```
