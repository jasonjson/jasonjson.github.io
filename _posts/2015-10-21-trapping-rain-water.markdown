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
[reference](http://blog.csdn.net/linhuanmars/article/details/20888505)

``` java
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        // write your code here
        if (heights == null || heights.length == 0) return 0;

        int[] container = new int[heights.length];
        int max = 0, result = 0;
        for (int i = 0; i < heights.length; i++) {
            container[i] = max;
            //record the max length on the left
            max = Math.max(max, heights[i]);
        }
        max = 0;
        for (int i = heights.length - 1; i >= 0; i--) {
            container[i] = Math.min(max, container[i]);//find the min between left max and rightmax, max is actually max on the right
            max = Math.max(max, heights[i]); //update max for i
            int diff = container[i] - heights[i];
            result +=  diff > 0 ? diff : 0;
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #scan A both from left to right and right to left, record the largest seen during
        #the scan; then for each position the water level should be the min of the 2 large value.

        if not height:
            return 0

        left_max = []
        ret = left_height = right_height = 0

        for h in height:
            left_max.append(left_height)
            left_height = max(left_height, h)

        for h in reversed(height):
            min_height = min(left_max.pop(), right_height)
            right_height = max(right_height, h)
            water = min_height - h
            ret += water if water > 0 else 0

        return ret
```
