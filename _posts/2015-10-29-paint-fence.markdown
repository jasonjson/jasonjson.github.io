---
layout: post
title: 276 - Paint Fence
date: 2015-10-29 15:23:28.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**There is a fence with n posts, each post can be painted with one of the k colors. You have to paint all the posts such that no more than two adjacent fence posts have the same color. Return the total number of ways you can paint the fence.**
[READ MORE](https://leetcode.com/discuss/56146/dynamic-programming-c-o-n-time-o-1-space-0ms)


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

``` python
class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        same_colors = k
        diff_colors = k * (k - 1)
        for i in xrange(3, n + 1):
        #To every sameCase and diffCase we can add a new post with different color as the last one. We have k-1 color options for the last one. To every diffCase we can add a new post with the same color as the last one to not generate violation - no more than 2 adjacent fence posts have the same color.
            diff_colors, same_colors = (diff_colors + same_colors) * (k - 1), diff_colors
        return diff_colors + same_colors
```
