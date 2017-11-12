---
layout: post
title: 398 - Random Pick Index
date: 2017-11-12
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.**


```python
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """

        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        count = 0
        ret = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == 1:
                    ret = i
        return ret
```
