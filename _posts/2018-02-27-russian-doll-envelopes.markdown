---
layout: post
title: 354 - Russian Doll Envelopes
date: 2018-02-27
tags:
- Leetcode
categories:
- Array
author: Jason
---
**You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope. What is the maximum number of envelopes can you Russian doll? (put one inside other)**


```python
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x: (x[0], -x[1]))
        ret = []

        for (_, b) in envelopes:
            index = self.find_index(ret, b)
            if index < len(ret):
                ret[index] = b
            else:
                ret.append(b)
        return len(ret)

    def find_index(self, nums, num):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
