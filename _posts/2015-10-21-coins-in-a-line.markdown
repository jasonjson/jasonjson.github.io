---
layout: post
title: Coins in a Line
date: 2015-10-21 13:25:45.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466755553;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:480;}i:1;a:1:{s:2:"id";i:1081;}i:2;a:1:{s:2:"id";i:1136;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins. Could you please decide the first play will win or lose?</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
