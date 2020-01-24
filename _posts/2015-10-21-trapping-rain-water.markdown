---
layout: post
title: 42 - Trapping Rain Water
date: 2015-10-21 14:41:08.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining**.

``` python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ret = 0
        left_max = [0]
        for i in range(1, len(height)):
            left_max.append(max(height[i - 1], left_max[-1]))

        right_max = 0
        for i in reversed(range(len(height) - 1)):
            right_max = max(right_max, height[i + 1])
            ret += max(0, min(right_max, left_max[i]) - height[i])
        return ret
```
