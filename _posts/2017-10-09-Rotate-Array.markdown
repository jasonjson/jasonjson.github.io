---
layout: post
title: Rotate Array
date: 2017-10-09
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Rotate an array of n elements to the right by k steps. For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].**


```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
```
