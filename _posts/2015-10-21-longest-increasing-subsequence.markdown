---
layout: post
title: Longest Increasing Subsequence
date: 2015-10-21 12:53:11.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
- Subarray
author: Jason
---
<p><strong><em>Given a sequence of integers, find the longest increasing subsequence (LIS). You code should return the length of the LIS.</em></strong></p>


<p><a href="http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/">read more</a></p>

``` java
public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length, len = 1;
        int[] seq = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                seq[i] = nums[i];
            } else if (nums[i] < seq[0]) {
                seq[0] = nums[i];
            } else if (nums[i] > seq[len - 1]) {
                seq[len++] = nums[i];
            } else {
                seq[findIndex(nums, 0, len - 1, nums[i])] = nums[i];
            }
        }
        return len;
    }
    
    public int findIndex(int[] nums, int lo, int hi, int key) {
    //find the index of first element in the array that is larger than key
        while (lo + 1 < hi) {// lo + 1...
            int mid = (lo + hi) / 2;
            if (nums[mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return hi;
    }
}
```
``` java
public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length, maxLen = 0;
        
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        //dp[i] indicates the LIS with ith element as the end, so it's at least 1, 
        //key : nums[i] must be the last element in the increasing subsequence
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] <= nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);                    
                }
            }
            maxLen = Math.max(maxLen, dp[i]);//only update global max in outmost loop
            //dp[i]是指以nums[i]结尾的LIS,所以括号里不是dp[i-1],必须以nums[i]结尾,
            //dp[i]是local max, maxLen是global_max
        }
        return maxLen;
    }
}
```
