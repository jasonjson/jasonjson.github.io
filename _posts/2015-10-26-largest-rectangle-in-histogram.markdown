---
layout: post
title: 84 - Largest Rectangle in Histogram
date: 2015-10-26 22:24:05.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.**

``` python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(0)
        ret = 0
        stack = [-1]
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ret = max(ret, h * w)
            stack.append(i)
        return ret
```
