---
layout: post
title: Climbing Stairs
date: 2015-10-21 12:26:49.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455392957;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:479;}i:1;a:1:{s:2:"id";i:388;}i:2;a:1:{s:2:"id";i:991;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param n: An integer
     * @return: An integer
     */
    public int climbStairs(int n) {
        //state: dp[i]
        //function: dp[i] = dp[i-1][i-2]
        //initialization dp[0] = 1, dp[1] = 1
        //answer: dp[n]
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}
</pre>
<p>[/expand]</p>
