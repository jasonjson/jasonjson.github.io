---
layout: post
title: 162 - Find Peak Element
date: 2015-10-21 02:28:54.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**A peak element is an element that is greater than its neighbors. Given an input array where num[i] !=  num[i+1], find a peak element and return its index. The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. You may imagine that num[-1] = num[n] = -inf. For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.**

``` python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid1 = (lo + hi) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                lo = mid2
            else:
                hi = mid1
        return lo
```
