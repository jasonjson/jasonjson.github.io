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
        if not nums:
            return

        red, blue = 0, len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                i -= 1
            i += 1
```
