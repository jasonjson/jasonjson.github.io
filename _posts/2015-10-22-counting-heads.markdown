---
layout: post
title: Counting heads
date: 2015-10-22 15:19:20.000000000 -04:00
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given integers n and k, along with p1, p2, · · · , pn ∈ [0, 1], you want to determine the probability of obtaining exactly k heads when n biased coins are tossed independently at random, where pi is the probability that the ith coin comes up heads. Give an O(n2) algorithm for this task. Assume you can multiply and add two numbers in [0,1] in O(1) time.</em></strong></p>

``` java
class Solution {
    public static void main(String[] args) {
        double[] P = {.5,.5,.5,.5,.5};
        System.out.println(countHead(P, 5));
    }
    public static double countHead(double[] P, int k) {
        if (P == null || P.length == 0) return 0;

        int n = P.length;
        double[][] dp = new double[n + 1][k + 1];
        //dp[i][j] toss i coins with j heads

        dp[0][0] = 1;//important!!
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (j > i) {
                    break;
                }//the number of heads can't exceed the number of coins
                dp[i][j] = dp[i - 1][j - 1] * P[i - 1] + dp[i - 1][j] * (1 - P[i - 1]);
                //we are only using dp[0][0] and dp[0][1] for i == 1 and j == 1
                //so there is no need to initialize dp[0][j] or dp[i][0]
            }
        }
        return dp[n][k];
    }
}
```
