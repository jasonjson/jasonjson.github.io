---
layout: post
title: 518 - Coin Change 2
date: 2020-01-25
tags:
- Leetcode
categories:
- DP
author: Jason
---
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
        # the order of coin dose not matter, so it cannot be in the inner loop
            for num in range(coin, amount + 1):
                dp[num] += dp[num - coin]
        return dp[-1]
```
