---
layout: post
title: 315 - Count of Smaller Numbers After Self
date: 2015-12-07 18:21:09.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].**

``` python
from bisect import bisect_left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        sort, ret = [], []
        for num in reversed(nums):
            index = bisect_left(sort, num)
            sort.insert(index, num)
            ret.append(index)
        return list(reversed(ret))

    def helper(self, sort, num):
        lo, hi = 0, len(sort) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if num > sort[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
