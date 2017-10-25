---
layout: post
title: 279 - Perfect Squares
date: 2015-10-28 11:33:33.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n. For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.**


``` java
public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int nearest = (int)Math.sqrt(i), min = Integer.MAX_VALUE;
            for (int j = nearest; j >= 1; j--) {
            //min代表了0到i-j^2能取到的最小数量
                min = Math.min(min, dp[i - j * j]);
            }
            dp[i] = min + 1;//这个1就是留给j * j的
        }
        return dp[n];
    }
}
```

``` python
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        for i in xrange(1, n + 1):
            nearest, prev_min = int(math.sqrt(i)), i
            for j in reversed(xrange(1, nearest + 1)):
                prev_min = min(prev_min, dp[i - j * j])
            dp[i] = prev_min + 1
        return dp[-1]
```
