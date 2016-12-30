---
layout: post
title: Coins in a Line II
date: 2015-10-21 13:26:15.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:2:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466754912;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:479;}i:1;a:1:{s:2:"id";i:1081;}i:2;a:1:{s:2:"id";i:388;}}}s:32:"067f18eb200b3707d5903529fe235b3b";a:2:{s:7:"expires";i:1466755569;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1081;}i:1;a:1:{s:2:"id";i:388;}i:2;a:1:{s:2:"id";i:1136;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins. Could you please decide the first player will win or lose?</em></strong></p>
<p>[expand title = "dp"]</p>
<pre>
public class Solution {
    /**
     * @param values: an array of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        if (values == null || values.length <= 2) return true;
        
        int n = values.length;
        int[] dp = new int[n+1];
        dp[1] = values[n-1];
        dp[2] = values[n-1] + values[n-2];
        dp[3] = values[n-2] + values[n-3];
        for (int i = 4; i <= n; i++) {
            int pick_one = values[n-i] + Math.min(dp[i-2], dp[i-3]);
            int pick_two = values[n-i] + values[n-i+1] + Math.min(dp[i-3], dp[i-4]);
            dp[i] = Math.max(pick_one, pick_two);
        }
        int sum = 0;
        for (int value : values) {
            sum += value;
        }
        return dp[n] > sum - dp[n];
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="greedy"]</p>
<pre>
public class Solution {
    /**
     * @param values: an array of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        int sum1 = 0, sum2 = 0, n = values.length;
        boolean turn = true;
        
        for (int i = 0; i < n; i++) {
            if (turn) {
                sum1 += values[i];
                if (i + 1 < n && values[i+1] >= values[i]) {
                    //if the value of second coin is larger than the fisrt coin
                    sum1 += values[++i];
                }
            } else {
                sum2 += values[i];
                if (i + 1 < n && values[i+1] >= values[i]) {
                    sum2 += values[++i];
                }
            }
            turn = !turn;
        }
        
        return sum1 > sum2;
    }
}
</pre>
<p>[/expand]</p>
