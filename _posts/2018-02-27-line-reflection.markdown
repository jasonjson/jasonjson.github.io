---
layout: post
title: 356 - Line Reflection
date: 2018-02-27
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not points:
            return True

        point_set = set()
        summation = max(points, key = lambda x: x[0])[0] + min(points, key = lambda x: x[0])[0]
        for (a, b) in points:
            point_set.add(str(a) + "c" + str(b))

        for (a, b) in points:
            mirror_point = str(summation - a) + "c" + str(b)
            if mirror_point not in point_set:
                return False
        return True
```
