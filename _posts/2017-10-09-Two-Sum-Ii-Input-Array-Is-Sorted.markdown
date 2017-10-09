---
layout: post
title: 167 - Two Sum Ii Input Array Is Sorted
date: 2017-10-09
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number. The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based. You may assume that each input would have exactly one solution and you may not use the same element twice.**


```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not numbers:
            return []

        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            summation = numbers[lo] + numbers[hi]
            if summation < target:
                lo += 1
            elif summation > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        return []
```
