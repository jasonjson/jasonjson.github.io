---
layout: post
title: Coin Change
date: 2016-01-03 19:24:01.000000000 -05:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468753631;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1081;}i:1;a:1:{s:2:"id";i:923;}i:2;a:1:{s:2:"id";i:557;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
