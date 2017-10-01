---
layout: post
title: Maximum Size Subarray Sum Equals k
date: 2016-01-05 12:18:15.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- Data Structure
author: Jason
---
<p><strong><em>Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.</em></strong></p>


``` java
public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if (nums == null || nums.length == 0) return 0;
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum = 0, len = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum == k) {
                len = Math.max(len, i + 1);
            } else if (map.containsKey(sum - k)) {
                len = Math.max(len, i - map.get(sum - k));
            } 
            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return len;
    }
}
```
