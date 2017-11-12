---
layout: post
title: 384 - Shuffle An Array
date: 2017-11-12
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Shuffle a set of numbers without duplicates.**


```python
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        ret = copy.deepcopy(self.nums)
        for i in xrange(len(self.nums)):
            #every num can switch with every number before it and itself
            j = random.randint(0, i)
            ret[i], ret[j] = ret[j], ret[i]
        return ret
```
