---
layout: post
title: 659 - Split Array Into Consecutive Subsequences
date: 2020-02-02
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

```python
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False

        left = Counter(nums)
        end = Counter()
        for num in nums:
            if left[num] == 0:
                continue
            left[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True
```
