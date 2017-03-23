---
layout: post
title: Trapping Rain Water
date: 2015-10-21 14:41:08.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.</em></strong></p>


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
    }//http://blog.csdn.net/linhuanmars/article/details/20888505
}

```
