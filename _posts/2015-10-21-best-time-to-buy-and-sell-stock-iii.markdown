---
layout: post
title: Best Time to Buy and Sell Stock III
date: 2015-10-21 12:48:00.000000000 -04:00
tags:
- Algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions.</em></strong></p>


``` java
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
```
