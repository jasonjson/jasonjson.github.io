---
layout: post
title: Container With Most Water
date: 2015-10-21 13:26:44.000000000 -04:00
tags:
- Algorithm
categories:
- Brain Teaser
author: Jason
---
**Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.**


``` java
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: an integer
     */
    public int maxArea(int[] heights) {
        if (heights == null || heights.length == 0) return 0;

        int result = 0, left = 0, right = heights.length - 1;
        while (left < right) {
            result = Math.max(result, (right - left) * Math.min(heights[left], heights[right]));
            if (heights[left] < heights[right]) {
                left ++;
            } else {
                right --;
            }
        }
        return result;
    }//https://leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm
    //http://www.cnblogs.com/tenosdoit/p/3812880.html
}
```

``` python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        ret = 0
        while left < right:
            ret = max(ret, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ret
```
