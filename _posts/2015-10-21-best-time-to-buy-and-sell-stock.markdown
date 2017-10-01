---
layout: post
title: 121 - Best Time to Buy and Sell Stock
date: 2015-10-21 12:46:21.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.**


``` java
public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        // write your code here
        if (prices == null || prices.length <= 1) return 0;

        int min_price = prices[0], profit = 0;
        for (int i = 1; i < prices.length; i++) {
            profit = Math.max(profit, prices[i] - min_price);
            min_price = Math.min(min_price, prices[i]);
        }
        return profit;
    }
}
```

``` python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        min_buy = prices[0]
        profit = 0
        for i, price in enumerate(prices[1:]):
            profit = max(profit, price - min_buy)
            min_buy = min(min_buy, price)
        return profit
```
