---
layout: post
title: Best Time to Buy and Sell Stock with Cooldown
date: 2015-11-24 09:18:49.000000000 -05:00
tags:
- Algorithm
categories:
- Dynamic Programming
author: Jason
---
**Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again). After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)**
[reference](https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-iv.html)


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

``` python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        #sell[i] 表示第i天未持股时，获得的最大利润，buy[i]表示第i天持有股票时，获得的最大利润。
        #对于sell[i]，最大利润有两种可能，一是今天没动作跟昨天未持股状态一样，二是今天卖了股票，所以状态转移方程如下：
        #sell[i] = max{sell[i - 1], buy[i-1] + prices[i]}
        #对于buy[i]，最大利润有两种可能，一是今天没动作跟昨天持股状态一样，二是前天卖了股票，今天买了股票，
        #因为 cooldown 只能隔天交易，所以今天买股票要追溯到前天的状态。状态转移方程如下：
        #buy[i] = max{buy[i-1], sell[i-2] - prices[i]}
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        buy[0] = -prices[0]
        for i in xrange(1, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            tmp = sell[i - 2] if i > 1 else 0
            buy[i] = max(buy[i - 1], tmp - prices[i])
        return sell[-1]
```
