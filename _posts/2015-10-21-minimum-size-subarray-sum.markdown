---
layout: post
title: Minimum Size Subarray Sum
date: 2015-10-21 14:31:53.000000000 -04:00
categories:
- Integer
- Subarray
author: Jason
---
<p><strong><em>Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s. If there isn't one, return -1 instead.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, sum = 0, len = nums.length + 1;
        for (int i = start; i < nums.length; i++) {
            sum += nums[i];
            while (sum >= s) {
                len = Math.min(len, i - start + 1);
                sum -= nums[start++];//先从sum减去再increment start,不能弄反
                //不论减去后sum是正是负都没关系，已经记录了len
            }            
        }
        return len == nums.length + 1 ? -1 : len;
    }
}
```
