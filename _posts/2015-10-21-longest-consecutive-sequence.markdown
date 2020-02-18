---
layout: post
title: 128 - Longest Consecutive Sequence
date: 2015-10-21 14:26:41.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an unsorted array of integers, find the length of the longest consecutive elements sequence.**

``` python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        for num in nums:
            left, right = num, num + 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1
            ret = max(ret, right - left - 1)
        return ret
```
