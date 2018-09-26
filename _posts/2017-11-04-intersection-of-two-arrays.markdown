---
layout: post
title: 349 - Intersection Of Two Arrays
date: 2017-11-04
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given two arrays, write a function to compute their intersection. Each element in the result must be unique. The result can be in any order.**


```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1) & set(nums2))
```
