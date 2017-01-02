---
layout: post
title: Maximum Subarray II
date: 2015-10-21 12:51:32.000000000 -04:00
categories:
- Dynamic Programming
- Subarray
author: Jason
---
<p><strong><em>Given an array of integers, find two non-overlapping subarrays which have the largest sum. The number in each subarray should be contiguous. Return the largest sum.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<integer> nums) {
        if (nums == null || nums.size() == 0) return 0;
        
        int n = nums.size(), local = 0, max = Integer.MIN_VALUE;
        int[] left_max = new int[n];
        for (int i = 0; i < n - 1; i++) {
            local = Math.max(local, 0) + nums.get(i);//必须以nums.get(i)结尾
            if (i == 0) {
                left_max[i] = local;
            } else {
                left_max[i] = Math.max(left_max[i-1], local);
            }
        }
        
        local = 0;
        int right_max = Integer.MIN_VALUE;
        for (int i = n - 1; i > 0; i--) {
            local = Math.max(local, 0) + nums.get(i);
            right_max = Math.max(right_max, local);//不需要单独处理i == n - 1,但是right_max 得设为最小值,要保证right_max == local 当 i == n - 1 时
            max = Math.max(max, right_max + left_max[i - 1]);
        }
        return max;
    }
}
```
