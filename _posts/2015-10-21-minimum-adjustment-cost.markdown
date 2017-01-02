---
layout: post
title: Minimum Adjustment Cost
date: 2015-10-21 14:32:27.000000000 -04:00
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target. If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|</em></strong></p>

``` java
public class Solution {
    public int MinAdjustmentCost(ArrayList<integer> A, int target) {
        if (A == null || A.size() == 0) return 0;
        
        int max = 0, result = Integer.MAX_VALUE;
        for (int num : A) {
            max = Math.max(max, num);
        }
        int[][] dp = new int[A.size() + 1][max + 1];
        for (int i = 1; i <= A.size(); i++) {
            for (int j = 0; j <= max; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int l = Math.max(0, j - target); l <= Math.min(max, j + target); l++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][l] + Math.abs(A.get(i - 1) - j));
                }
            }
        }        
        for (int j = 0; j <= max; j++) {
            result = Math.min(result, dp[A.size()][j]);
        }
        return result;
    }
}
```
