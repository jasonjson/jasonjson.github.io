---
layout: post
title: 322 - Coin Change
date: 2016-01-03 19:24:01.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.**

``` python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = 2 ** 31 - 1
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != 2 ** 31 - 1 else -1
```
