---
layout: post
title: Post Office Problem
date: 2015-10-26 15:59:07.000000000 -04:00
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>On one line there are n houses. Give you an array of integer means the the position of each house. Now you need to pick k position to build k post office, so that the sum distance of each house to the nearest post office is the smallest. Return the least possible sum of all distances between each village and its nearest post office.</em></strong></p>

``` java
public class Solution {
    /**
     * @param A an integer array
     * @param k an integer
     * @return an integer
     */
    public int postOffice(int[] A, int k) {
        // Write your code here
        if (A == null || A.length == 0) return 0;
        
        int n = A.length;
        if (k >= n) return 0;
        Arrays.sort(A);
        int[][] dist = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int mid = (i + j) / 2;
                for (int l = i; l <= j; l++) {
                    dist[i][j] += Math.abs(A[l - 1] - A[mid - 1]);
                }
            }
        }
        int[][] dp = new int[k + 1][n + 1];
        for (int j = 1; j <= n; j++) {
            dp[1][j] = dist[1][j];
        }//initialization 
        for (int i = 2; i <= k; i++) {
            for (int j = i; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int l = j; l >= 1; l--) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][l - 1] + dist[l][j]);
//divide 0 - i villages in two parts, place j - 1 post offices in 0 to l villages and 1 post office between l + 1 and i villages
                }
            }
        }
        return dp[k][n];
    }
}
```
