---
layout: post
title: Maximum Product Subarray
date: 2015-10-21 14:30:37.000000000 -04:00
tags:
- Leetcode
categories:
- Subarray
author: Jason
---
<p><strong><em>Find the contiguous subarray within an array (containing at least one number) which has the largest product.</em></strong></p>


``` java
public class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int min = 1, max = 1, global = Integer.MIN_VALUE;
        for (int n : nums) {
            int temp = max;
            max = Math.max(max * n, Math.max(min * n, n));
            min = Math.min(temp * n, Math.min(min * n, n));
            global = Math.max(max, global);
        }
        return global;
    }
}//http://blog.csdn.net/linhuanmars/article/details/39537283
```
