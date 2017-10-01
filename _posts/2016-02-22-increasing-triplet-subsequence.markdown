---
layout: post
title: Increasing Triplet Subsequence
date: 2016-02-22 23:25:30.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.</em></strong></p>


``` java
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                if (dp[i] >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
}
```
``` java
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        
        int min = Integer.MAX_VALUE, secondMin = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num <= min) {
                min = num;//we need to include "=" here, otherwise secondMin might get updated when num == min
            } else if (num < secondMin) {
                secondMin = num;
            } else if (num > secondMin) {
                return true;
            }
        }
        return false;
    }
}
```
