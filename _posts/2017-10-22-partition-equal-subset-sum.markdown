---
layout: post
title: 416 - Partition Equal Subset Sum
date: 2017-10-22
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.**
Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers. If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.


```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        summation = sum(nums)
        if summation % 2 != 0:
            return False
        summation /= 2
        dp = [False] * (summation + 1)
        dp[0] = True
        for num in nums:
            for i in reversed(xrange(1, summation + 1)):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[-1]
```
