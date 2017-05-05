---
layout: post
title: Max Consecutive Ones
date: 2017-05-04
tags:
- Algorithm
categories:
- Array
author: Jason
---
**Given a binary array, find the maximum number of consecutive 1s in this array.**

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                ret = max(ret, count)
        return ret
```
