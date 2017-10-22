---
layout: post
title: 410 - Split Array Largest Sum
date: 2017-10-22
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.**


```python
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums:
            return 0

        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) / 2
            if self.is_valid(nums, mid, m):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def is_valid(self, nums, summation, m):
        count, target = 1, 0
        for num in nums:
            target += num
            if target > summation:
                target = num
                count += 1
                if count > m:
                    return False
        return True
```
