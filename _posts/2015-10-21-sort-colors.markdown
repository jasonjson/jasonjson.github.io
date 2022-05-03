---
layout: post
title: 75 - Sort Colors
date: 2015-10-21 14:37:34.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.**

``` python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        1. array[0 to lo-1] = 0 is present
        2. array[lo to mid-1] = 1 is present
        3. array[mid to hi-1] = unknown
        4. array[hi to n(size of list)] = 2 is present
        """
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
```
