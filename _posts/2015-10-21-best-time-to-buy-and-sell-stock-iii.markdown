---
layout: post
title: Best Time to Buy and Sell Stock III
date: 2015-10-21 12:48:00.000000000 -04:00
type: post
published: true
status: publish
categories:
- Dynamic Programming
tags: []
meta:
  _spost_short_title: ''
  _wpas_done_all: '1'
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467725331;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1626;}i:1;a:1:{s:2:"id";i:400;}i:2;a:1:{s:2:"id";i:402;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) return 0;
        
        int n = prices.length, maxProfit = 0;
        int[] leftProfit = new int[n];
        for (int i = 1, min_price = prices[0]; i < n; i++) {
            leftProfit[i] = Math.max(leftProfit[i-1], prices[i] - min_price);
            min_price = Math.min(min_price, prices[i]);
        }
        
        int rightProfit = 0;
        for (int i = n - 2, max_price = prices[n - 1]; i >= 0; i--) {
            rightProfit = Math.max(rightProfit, max_price - prices[i]);
            max_price = Math.max(max_price, prices[i]);
            maxProfit = Math.max(maxProfit, rightProfit + leftProfit[i]);
        }
        return maxProfit;
    }
};
</pre>
<p>[/expand]</p>
