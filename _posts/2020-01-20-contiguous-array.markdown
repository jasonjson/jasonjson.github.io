---
layout: post
title: 525 - Contiguous Array
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count_table = {0: 0}
        count = ret = 0
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            elif num == 1:
                count += 1
            if count in count_table:
                ret = max(ret, i - count_table[count])
            else:
                count_table[count] = i
        return ret
```
