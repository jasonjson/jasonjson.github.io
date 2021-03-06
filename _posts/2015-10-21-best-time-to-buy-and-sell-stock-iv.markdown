---
layout: post
title: Best Time to Buy and Sell Stock IV
date: 2015-10-21 12:48:31.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most k transactions.</em></strong></p>


<p>传统的动态规划我们会这样想，到第i天时进行j次交易的最大收益，要么等于到第i-1天时进行j次交易的最大收益（第i天价格低于第i-1天的价格），要么等于到第i-1天时进行j-1次交易，然后第i天进行一次交易（第i天价格高于第i-1天价格时）。于是得到动规方程如下（其中diff = prices[i] – prices[i – 1]）：</p>
<p>profit[i][j] = max(profit[i – 1][j], profit[i – 1][j – 1] + diff)</p>
看起来很有道理，但其实不对，为什么不对呢？因为diff是第i天和第i-1天的差额收益，如果第i-1天当天本身也有交易呢（也就是说第i-1天刚卖出了股票，然后又买入等到第i天再卖出），那么这两次交易就可以合为一次交易，这样profit[i – 1][j – 1] + diff实际上只进行了j-1次交易，而不是最多可以的j次，这样得到的最大收益就小了。</p>
<p>那么怎样计算第i天进行交易的情况的最大收益，才会避免少计算一次交易呢？我们用一个局部最优解和全局最有解表示到第i天进行j次的收益，这就是该动态规划的特殊之处。</p>
<p>用local[i][j]表示到达第i天时，最多进行j次交易的局部最优解；用global[i][j]表示到达第i天时，最多进行j次的全局最优解。它们二者的关系如下（其中diff = prices[i] – prices[i – 1]）：</p>
<p>local[i][j] = max(global[i – 1][j – 1] , local[i – 1][j] + diff)</p>
global[i][j] = max(global[i – 1][j], local[i][j])</p>
local[i][j]和global[i][j]的区别是：local[i][j]意味着在第i天一定有交易（卖出）发生，当第i天的价格高于第i-1天（即diff > 0）时，那么可以把这次交易（第i-1天买入第i天卖出）跟第i-1天的交易（卖出）合并为一次交易，即local[i][j]=local[i-1][j]+diff；当第i天的价格不高于第i-1天（即diff&lt;=0）时，那么local[i][j]=global[i-1][j-1]+diff，而由于diff&lt;=0，所以可写成local[i][j]=global[i-1][j-1]。global[i][j]就是我们所求的前i天最多进行k次交易的最大收益，可分为两种情况：如果第i天没有交易（卖出），那么global[i][j]=global[i-1][j]；如果第i天有交易（卖出），那么global[i][j]=local[i][j]。</p>
``` java
class Solution {
    /**
     * @param k: An integer
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
//http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html
//http://www.cnblogs.com/grandyang/p/4295761.html
    public int maxProfit(int k, int[] prices) {
        if (prices == null || prices.length == 0) return 0;
        
        int n = prices.length, profit = 0;
        if (k > n / 2) {
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    profit += prices[i] - prices[i - 1];
                }
            }
            return profit;
        }
        
        int[] local = new int[k + 1], global = new int[k + 1];        
        for (int i = 1; i < n; i ++) {
            int diff = prices[i] - prices[i - 1];
            for (int j = 1; j <= k; j++) {
                local[j] = Math.max(global[j - 1], local[j] + diff);
                global[j] = Math.max(local[j], global[j]);
            }
        }
        return global[k];
    }
};
```
