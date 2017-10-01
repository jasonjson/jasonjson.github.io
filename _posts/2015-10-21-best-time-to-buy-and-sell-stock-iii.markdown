---
layout: post
title: 123 - Best Time to Buy and Sell Stock III
date: 2015-10-21 12:48:00.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions.**


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

``` python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        ret = 0
        left_profit = [0] * len(prices)
        min_buy = prices[0]
        for i in xrange(1, len(prices)):
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        right_profit, max_sell = 0, prices[-1]
        for i in reversed(xrange(len(prices) - 1)):
            right_profit = max(right_profit, max_sell - prices[i])
            max_sell = max(max_sell, prices[i])
            ret = max(ret, left_profit[i] + right_profit)
        return ret
```
