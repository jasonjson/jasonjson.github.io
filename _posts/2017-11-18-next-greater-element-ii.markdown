---
layout: post
title: 503 - Next Greater Element II
date: 2017-11-18
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.**


```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        stack, ret = [], [-1] * len(nums)
        for i in xrange(2 * len(nums)):
            num = nums[i % len(nums)]
            while stack and nums[stack[-1]] < num:
                ret[stack.pop()] = num
            if i < len(nums):
                stack.append(i)
        return ret
```
