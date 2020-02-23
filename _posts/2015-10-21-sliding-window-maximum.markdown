---
layout: post
title: 239 - Sliding Window Maximum
date: 2020-01-15
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving**

``` python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        ret, queue = [], []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i - queue[0] == k:
                queue.pop(0)
            ret.append(nums[queue[0]])
        return ret[k-1:]
```
