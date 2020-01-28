---
layout: post
title: 300 - Longest Increasing Subsequence
date: 2015-10-21 12:53:11.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a sequence of integers, find the longest increasing subsequence (LIS). You code should return the length of the LIS.**

``` python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        ret = []
        for num in nums:
            index = self.find_index(ret, num)
            if index < len(ret):
                ret[index] = num
            else:
                ret.append(num)
        return len(ret)

    def find_index(self, nums, num):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
