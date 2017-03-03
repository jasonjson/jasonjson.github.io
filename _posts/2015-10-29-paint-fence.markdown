---
layout: post
title: Paint Fence
date: 2015-10-29 15:23:28.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>There is a fence with n posts, each post can be painted with one of the k colors. You have to paint all the posts such that no more than two adjacent fence posts have the same color. Return the total number of ways you can paint the fence.</em></strong></p>


<p><a href="https://leetcode.com/discuss/56146/dynamic-programming-c-o-n-time-o-1-space-0ms">Read more</a></p>
``` java
public class Solution {
    //Need two one-dimensional array dp1 and dp2, dp1[i] means the number of solutions when the color of last two fences (whose indexes are i-1,i-2) are same. dp2[i] means the number of solutions when the color of last two fences are different.
    //dp1[i]=dp2[i-1],
    //dp2[i]=(k-1)(dp1[i-1]+dp2[i-1]) =(k-1)(dp2[i-2]+dp2[i-1])
    //by substitution, dp1[i] + dp2[i] = (k-1)(dp1[i-2] + dp2[i-2] + dp1[i-1] + dp2[i-1])
    public int numWays(int n, int k) {
        if (n == 0 || k == 0) return 0;
        if (n == 1) return k;
        int[] dp = new int[n + 1];
        dp[1] = k;
        dp[2] = k * k;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1);
        }
        return dp[n];
    }
}
```
