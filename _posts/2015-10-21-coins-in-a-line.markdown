---
layout: post
title: Coins in a Line
date: 2015-10-21 13:25:45.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins. Could you please decide the first play will win or lose?</em></strong></p>


``` java
public class Solution {
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        if (n == 0) return false;
        boolean[] dp = new boolean[n + 1];
        dp[0] = false;
        dp[1] = true;
        for (int i = 2; i <= n; i++) {
            dp[i] = ! (dp[i-1] && dp[i-2]);
            //the second player can't get to the end 
            //no matter he takes one or two coins
        }
        return dp[n];
    }
}
```
