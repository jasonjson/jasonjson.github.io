---
layout: post
title: 198 - House Robber
date: 2015-10-21 14:15:26.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.**

``` python
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = no_rob = 0
        # rob:rob current house, no_rob: dont rob current house
        for num in nums:
            rob, no_rob = no_rob + num, max(rob, no_rob)
        return max(rob, no_rob)
```
