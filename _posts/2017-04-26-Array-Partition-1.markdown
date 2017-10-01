---
layout: post
title: Array Partition 1
date: 2017-04-26
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.**

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
```
