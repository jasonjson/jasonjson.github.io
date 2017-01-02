---
layout: post
title: Coin Change
date: 2016-01-03 19:24:01.000000000 -05:00
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.</em></strong></p>


``` java
public class Solution {
    public int coinChange(int[] coins, int amount) {
        if (coins == null || coins.length == 0) return -1;
        
        long[] dp = new long[amount + 1];
        //用long是因为amount可能为integer.MAX_VALUE
        for (int i = 1; i <= amount; i++) {
            dp[i] = Integer.MAX_VALUE;
            //不用用arrays.fill, dp[0] == 0
            for (int j = 0; j < coins.length; j++) {
                if (i >= coins[j]) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] >= Integer.MAX_VALUE ? -1 : (int)dp[amount];
    }
}
```
