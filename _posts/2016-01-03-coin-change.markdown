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


``` java
public class Solution {
    public int coinChange(int[] coins, int amount) {
        if (coins == null || coins.length == 0) return -1;

        long[] dp = new long[amount + 1];
        //用long是因为amount可能为integer.MAX_VALUE
        for (int i = 1; i <= amount; i++) {
            dp[i] = Integer.MAX_VALUE;
            //不用用arrays.fill, dp[0] == 0
            for (int j = 0; j < coins.length; j++) {
                if (i >= coins[j]) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] >= Integer.MAX_VALUE ? -1 : (int)dp[amount];
    }
}
```

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        ret = []
        coins.sort()
        self.helper(coins, [], ret, amount)
        return min([len(i) for i in ret] or [-1])

    def helper(self, coins, curr, ret, remain):
        if remain == 0:
            ret.append(curr[:])
            return
        for coin in coins:
            if coin <= remain:
                self.helper(coins, curr + [coin], ret, remain - coin)
```

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
