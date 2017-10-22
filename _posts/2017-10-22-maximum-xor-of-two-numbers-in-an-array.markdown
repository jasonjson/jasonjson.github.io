---
layout: post
title: 421 - Maximum Xor Of Two Numbers In An Array
date: 2017-10-22
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231. Find the maximum result of ai XOR aj, where 0 ≤ i, j < n. Could you do this in O(n) runtime?**


```python
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ret = mask = 0
        for i in reversed(xrange(32)):
            mask |= 1 << i
            same_prefix = set()
            for num in nums:
                same_prefix.add(num & mask)
            # now find out if there are two prefix with different i-th bit
            # if there is, the new max should be current max with one 1 bit at i-th position, which is candidate
            # and the two prefix, say A and B, satisfies:
            # A ^ B = candidate so we also have A ^ candidate = B or B ^ candidate = A
            # thus we can use this method to find out if such A and B exists in the set
            candidate = ret | (1 << i)
            for num in same_prefix:
                if num ^ candidate in same_prefix:
                    ret = candidate
                    break
        return ret
```
