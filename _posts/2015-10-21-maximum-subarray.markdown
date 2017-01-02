---
layout: post
title: Maximum Subarray
date: 2015-10-21 12:50:20.000000000 -04:00
categories:
- Subarray
author: Jason
---
<p><strong><em>Given an array of integers, find a contiguous subarray which has the largest sum.</em></strong></p>

``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */ 
    public int maxSubArray(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;
        
        int local = 0, max = Integer.MIN_VALUE;
        for (int num : nums) {
            local = Math.max(local + num, num);//num must be the last number in local
            max = Math.max(max, local);
        }
        return max;
    }
}
```
