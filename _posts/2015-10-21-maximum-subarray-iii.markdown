---
layout: post
title: Maximum Subarray III
date: 2015-10-21 12:52:17.000000000 -04:00
categories:
- Dynamic Programming
- Subarray
author: Jason
---
<p><strong><em>Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum. The number in each subarray should be contiguous. Return the largest sum.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer denote to find k non-overlapping subarrays
     * @return: An integer denote the sum of max k non-overlapping subarrays
     */
    public int maxSubArray(ArrayList<integer> nums, int k) {
        // write your code
        if (nums == null || nums.size() == 0) return 0;
                
        int n = nums.size();
        int[][] sum = new int[k + 1][n + 1];
        //from i elements pick k subarray
        for (int i = 1; i <= k; i++) {
            int local = Integer.MIN_VALUE;
            for (int j = i; j <= n; j++) {
                local = Math.max(local, sum[i-1][j-1]) + nums.get(j-1);
                if (j == i) {
                    sum[i][j] = local;
                } else {
                    sum[i][j] = Math.max(local, sum[i][j-1]);
                }
            }
        }
        return sum[k][n];
    }
}//http://hehejun.blogspot.com/2015/01/lintcodemaximum-subarray-iii.html
```
