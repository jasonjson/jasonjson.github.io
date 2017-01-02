---
layout: post
title: Maximum Subarray Difference
date: 2015-10-21 14:31:14.000000000 -04:00
categories:
- Dynamic Programming
- Subarray
author: Jason
---
<p><strong><em>Given an array with integers. Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest. Return the largest difference.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer indicate the value of maximum difference between two
     *          Subarrays
     */
    public int maxDiffSubArrays(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;
        //bug: typos !!!!
        int result = 0;
        int[] left_max = new int[nums.size()], left_min = new int[nums.size()];
        int local_max = 0, local_min = 0;
        for (int i = 0; i < nums.size(); i++) {
            local_max = Math.max(local_max + nums.get(i), nums.get(i));
            local_min = Math.min(local_min + nums.get(i), nums.get(i));
            if (i == 0) {
                left_max[i] = local_max;
                left_min[i] = local_min;
            } else {
                left_max[i] = Math.max(left_max[i-1], local_max);
                left_min[i] = Math.min(left_min[i-1], local_min);
            }
        }
        local_max = 0; local_min = 0;
        int last_max = 0, last_min = 0;
        //no need to create another int[] to store the globla max and min for right part
        for (int i = nums.size() - 1; i > 0; i--) {//> 0 not >= 0
            local_max = Math.max(local_max + nums.get(i), nums.get(i));
            local_min = Math.min(local_min + nums.get(i), nums.get(i));
            if (i == nums.size() - 1) {
                last_max = local_max;
                last_min = local_min;
            } else {
                last_max = Math.max(last_max, local_max);
                last_min = Math.min(last_min, local_min);
            }
            result = Math.max(result, Math.max(Math.abs(last_max - left_min[i-1]), Math.abs(left_max[i-1] - last_min)));
        }
        return result;
    }
}//http://blog.csdn.net/nicaishibiantai/article/details/44490241
```
