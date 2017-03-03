---
layout: post
title: Best Time to Buy and Sell Stock with Cooldown
date: 2015-11-24 09:18:49.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Say you have an array for which the ith element is the price of a given stock on day i.</p>

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:</p>
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</p>
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)</em></strong></p>
``` java
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length <= 1) return 0;
        int[] profit = new int[prices.length];
        profit[0] = 0;
        profit[1] = Math.max(0, prices[1] - prices[0]);
        int buy = Math.max(0 - prices[0], 0 - prices[1]);
        for (int i = 2; i < prices.length; i++) {
            //int temp = val + prices[i];
            profit[i] = Math.max(profit[i - 1], buy + prices[i]);//i天cooldown或i天卖
            buy = Math.max(buy, profit[i - 2] - prices[i]);
            //buy类似于buy[i]表示i天买的最大profit,可能是i天买prices[i]所以减去,也可能i-1天买
        }
        return profit[prices.length - 1];
    }
}
```
``` java
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length <= 1) return 0;
        int[] global = new int[prices.length];
        global[0] = 0;
        global[1] = Math.max(0, prices[1] - prices[0]);
        for (int i = 2; i < prices.length; i++) {
            int local = 0;
            for (int j = i; j >= 2; j--) {
                local = Math.max(local, global[j - 2] + prices[i] - prices[j]);
            }
            local = Math.max(local, Math.max(prices[i] - prices[0], prices[i] - prices[1]));
            global[i] = Math.max(local, global[i - 1]);
        }
        return global[prices.length - 1];
    }
}
```
