---
layout: post
title: 360 - Sort Transformed Array
date: 2016-01-20 18:05:25.000000000 -05:00
tags:
- OA
categories:
- Brain Teaser
author: Jason
---
**Given an equation y = ax^2 + bx + c, and sorted array X, output sorted Y.**


``` python
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        nums = [a * num * num + b * num + c for num in nums]
        left, right = 0, len(nums) - 1
        ret = [0] * len(nums)
        left_index, right_index = left, right
        while left <= right:
            if a > 0:
                if nums[left] < nums[right]:
                    ret[right_index] = nums[right]
                    right -= 1
                else:
                    ret[right_index] = nums[left]
                    left += 1
                right_index -= 1
            else:
                if nums[left] < nums[right]:
                    ret[left_index] = nums[left]
                    left += 1
                else:
                    ret[left_index] = nums[right]
                    right -= 1
                left_index += 1
        return ret
```
