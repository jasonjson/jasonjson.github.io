---
layout: post
title: Burst Balloons
date: 2015-11-29 20:36:44.000000000 -05:00
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.<br />

Find the maximum coins you can collect by bursting the balloons wisely.</em></strong></p>
<p><a href="https://leetcode.com/discuss/72216/share-some-analysis-and-explanations">read more</a></p>
``` java
public class Solution {
    public int maxCoins(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        int[] ballons = new int[nums.length + 2];
        int len = 1;
        for (int num : nums) {
            if (num > 0) {
                ballons[len++] = num;
            }
        }
        ballons[0] = ballons[len++] = 1;
        int[][] coins = new int[len][len];        
        for (int k = 3; k <= len; k++) {//there are at least three balloons
            for (int left = 0; left + k - 1 < len; left ++) {
                int right = left + k - 1;
                for (int i = left + 1; i < right; i ++) {
                    coins[left][right] = Math.max(coins[left][right], ballons[left] * ballons[i] * ballons[right] + coins[left][i] + coins[i][right]);
                }
            }
        }
        return coins[0][len - 1];
    }
}
```
