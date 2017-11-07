---
layout: post
title: 368 - Largest Divisible Subset
date: 2017-09-12
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0. If there are multiple solutions, return any subset is fine.**


``` python
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        index = [-1] * len(nums)
        max_count, start = 0, -1
        for i in xrange(len(nums)):
            for j in reversed(xrange(i)):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        index[i] = j
            if dp[i] > max_count:
                max_count = dp[i]
                start = i

        ret = []
        while start != -1:
            ret.append(nums[start])
            start = index[start]
        return ret
```
