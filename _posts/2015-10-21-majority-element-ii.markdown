---
layout: post
title: 229 - Majority Element II
date: 2015-10-21 02:40:45.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.**


``` python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        e1, e2, c1, c2 = 0, 1, 0, 0
        for num in nums:
            if num == e1:
                c1 += 1
            elif num == e2:
                c2 += 1
            elif c1 == 0:
                e1, c1 = num, 1
            elif c2 == 0:
                e2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (e1, e2) if nums.count(n) > len(nums) / 3]
```
