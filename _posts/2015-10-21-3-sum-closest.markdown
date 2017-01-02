---
layout: post
title: 3 Sum Closest
date: 2015-10-21 02:22:25.000000000 -04:00
categories:
- Integer
author: Jason
---
<p><strong><em>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.</em></strong></p>


``` java
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) return -1;
        
        Arrays.sort(nums);
        int n = nums.length;
        int result = nums[0] + nums[1] + nums[2];
        for (int i = 0; i + 2 < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int lo = i + 1, hi = n - 1;
            while (lo < hi) {
                if (lo > i + 1 && nums[lo] == nums[lo - 1]) {
                    lo++;
                    continue;
                } 
                if (hi < n - 1 && nums[hi] == nums[hi + 1]) {
                    hi--;
                    continue;
                }
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    lo++;
                } else {
                    hi--;
                }
                if (Math.abs(result - target) > Math.abs(sum - target)) {
                    result = sum;
                }
            }
        }
        return result;
    }
}
```
