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
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        container = [0] * len(height)
        max_height = ret = 0

        for i in range(len(height)):
            container[i] = max_height
            max_height = max(max_height, height[i])

        max_height = 0
        for i in reversed(range(len(height))):
            container[i] = min(container[i], max_height)
            max_height = max(max_height, height[i])
            diff = container[i] - height[i]
            ret += diff if diff > 0 else 0

        return ret
```
