---
layout: post
title: 377 - Combination Sum Iv
date: 2017-11-07
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.**


```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in xrange(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]
```
