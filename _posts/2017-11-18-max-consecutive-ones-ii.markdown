---
layout: post
title: 487 - Max Consecutive Ones Ii
date: 2017-11-18
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.**


```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        #keep a window with at most 1 zero
        lo = hi = zero = 0
        ret, k = 0, 1
        while hi < len(nums):
            if nums[hi] == 0:
                zero += 1
            while zero > k:
                if nums[lo] == 0:
                    zero -= 1
                lo += 1
            ret = max(ret, hi - lo + 1)
            hi += 1
        Return ret
```
