---
layout: post
title: 34 - Search for a Range
date: 2015-10-21 02:27:43.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given a sorted array of integers, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].**

``` python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                left = right = mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1, -1]
```
