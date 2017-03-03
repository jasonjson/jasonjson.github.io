---
layout: post
title: Paint House II
date: 2015-10-30 21:22:04.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.</em></strong></p>


``` java
public class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        
        int row = costs.length, col = costs[0].length;
        int[][] dp = new int[row][col];
        for (int j = 0; j < col; j++) {
            dp[0][j] = costs[0][j];
        }
        for (int i = 1; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int min = Integer.MAX_VALUE;
                for (int l = 0; l < col; l++) {
                    if (l != j) {
                        min = Math.min(min, dp[i - 1][l]);
                    }
                }
                dp[i][j] = min + costs[i][j];
            }
        }
        int result = Integer.MAX_VALUE;
        for (int j = 0; j < col; j++) {
            result = Math.min(result, dp[row - 1][j]);
        }
        return result;
    }
}
```
``` java
public class Solution {
    //Explanation: dp[i][j] represents the min paint cost from house 0 to house i when house i use color j; The formula will be dp[i][j] = Math.min(any k!= j| dp[i-1][k]) + costs[i][j]. Take a closer look at the formula, we don't need an array to represent dp[i][j], we only need to know the min cost to the previous house of any color and if the color j is used on previous house to get prev min cost, use the second min cost that are not using color j on the previous house. So I have three variable to record: prevMin, prevMinColor, prevSecondMin. and the above formula will be translated into: dp[currentHouse][currentColor] = (currentColor == prevMinColor? prevSecondMin: prevMin) + costs[currentHouse][currentColor].
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        int n = costs.length, k = costs[0].length;
        if (k == 1) return n == 1 ? costs[0][0] : -1;
        
        int preMin = 0, preSecMin = 0, preInd = -1;
        for (int i = 0; i < n; i++) {
            int min = Integer.MAX_VALUE, secMin = Integer.MAX_VALUE, index = -1;
            for (int j = 0; j < k; j++) {
                int cost = costs[i][j] + (j == preInd ? preSecMin : preMin);
                //i == 0,初始化cost = cost[i][j],只有第一次才执行
                if (index == -1) {
                    min = cost;
                    index = j;
                } else if (cost < min) {
                    secMin = min;
                    min = cost;
                    index = j;
                } else if (cost < secMin) {
                    secMin = cost;
                }
            }
            preMin = min;
            preSecMin = secMin;
            preInd = index;
        }
        return preMin;
    }
}
```
