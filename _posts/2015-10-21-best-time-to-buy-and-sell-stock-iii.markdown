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

``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left_min = prices[0]
        left_profit = [0] * len(prices)
        for i in range(1, len(prices)):
            left_profit[i] = max(left_profit[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

        right_max = prices[-1]
        right_profit = 0
        ret = 0
        for i in reversed(range(len(prices) - 1)):
            right_profit = max(right_profit, right_max - prices[i])
            right_max = max(right_max, prices[i])
            ret = max(ret, left_profit[i] + right_profit)
        return ret
```
