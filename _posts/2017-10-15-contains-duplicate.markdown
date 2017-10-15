---
layout: post
title: 217 - Contains Duplicate
date: 2017-10-15
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.**


```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False
        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            num_map[num] = 1
        return False
```
