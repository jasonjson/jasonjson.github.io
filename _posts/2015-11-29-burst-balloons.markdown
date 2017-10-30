---
layout: post
title: 312 - Burst Balloons
date: 2015-11-29 20:36:44.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent. Find the maximum coins you can collect by bursting the balloons wisely.**


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

``` python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        balloon = [1]
        for num in nums:
            if num > 0:
                balloon.append(num)
        balloon.append(1)
        size = len(balloon)
        dp = [[0] * size for i in xrange(size)]
        for i in xrange(3, size + 1):
            for left in xrange(size - i + 1):
                right = left + i - 1
                for j in xrange(left + 1, right):
                    dp[left][right] = max(dp[left][right], balloon[left] * balloon[j] * balloon[right] + dp[left][j] + dp[j][right])
        return dp[0][-1]
```
