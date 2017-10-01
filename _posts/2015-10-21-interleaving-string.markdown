---
layout: post
title: Interleaving String
date: 2015-10-21 12:49:37.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.</em></strong></p>


``` java
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1 == null && s2 == null && s3 == null) return true;
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        if (l1 == 0 && l2 == 0 && l3 == 0) return true;
        if (l1 + l2 != l3) return false;
        
        boolean[][] dp = new boolean[l1+1][l2+1];
        //dp[i][j] : s1.substring(0, i) and s2.substring(0, j) matches 
        //s3.substring(0, i+j-1)
        dp[0][0] = true;//base case !!
        for (int i = 1; i <= l1; i++) {
            dp[i][0] = s1.charAt(i-1) == s3.charAt(i-1) && dp[i-1][0];
        }
        
        for (int j = 1; j <= l2; j++) {
            dp[0][j] = s2.charAt(j-1) == s3.charAt(j-1) && dp[0][j-1];
        }
        
        for (int i = 1; i <= l1; i++) {
            for (int j = 1; j <= l2; j++) {
                boolean case1 = s1.charAt(i-1) == s3.charAt(i + j - 1) && dp[i-1][j];
                boolean case2 = s2.charAt(j-1) == s3.charAt(i + j - 1) && dp[i][j-1];
                dp[i][j] = case1 || case2;
            }
        }
        return dp[l1][l2];
    }
}
```
