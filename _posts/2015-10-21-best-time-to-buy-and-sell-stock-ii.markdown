---
layout: post
title: Best Time to Buy and Sell Stock II
date: 2015-10-21 12:46:57.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467724666;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1626;}i:1;a:1:{s:2:"id";i:400;}i:2;a:1:{s:2:"id";i:405;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        // write your code here
        if (prices == null || prices.length <= 1) return 0;
        //buy and sell stocks in one day is just like you wasted one chance of transaction. For example, if you bought on Day 1 and sell on Day 5 and bought on Day 5 and sell on Day 10. Profit is P5 - P1 + P10 - P5. It has the same profit as bought on day 1 and sell on day 10(P10 - P1).
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i-1];
            if (diff > 0) profit += diff;
        }
        return profit;
    }
};
</pre>
<p>[/expand]</p>
