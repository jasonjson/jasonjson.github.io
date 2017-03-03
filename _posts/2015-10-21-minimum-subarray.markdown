---
layout: post
title: Minimum Subarray
date: 2015-10-21 12:50:57.000000000 -04:00
tags: algorithm
categories:
- Subarray
author: Jason
---
<p><strong><em>Given an array of integers, find the subarray with smallest sum. Return the sum of the subarray.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;
        
        int min = Integer.MAX_VALUE, local = 0;
        for (int num : nums) {
            local = Math.min(local + num, num);
            min = Math.min(min, local);
        }
        return min;
    }
}
```
