---
layout: post
title: 213 - House Robber II
date: 2015-11-03 18:28:31.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street. Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.**

``` python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def helper(nums):
            prev = now = 0
            for num in nums:
                prev, now = now, max(prev + num, now)
            return now

        return max(helper(nums[:-1]), helper(nums[1:]))
```
