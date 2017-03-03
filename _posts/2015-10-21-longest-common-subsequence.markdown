---
layout: post
title: Longest Common Subsequence
date: 2015-10-21 12:44:53.000000000 -04:00
tags: algorithm
categories:
- String
author: Jason
---
<p><strong><em>Given two strings, find the longest common subsequence (LCS). Your code should return the length of LCS.</em></strong></p>


``` java
public class Solution {
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    public int longestCommonSubsequence(String A, String B) {
        // key: the sequence can be discrete
        if (A == null || A.length() == 0) return 0;
        if (B == null || B.length() == 0) return 0;
        
        int m = A.length(), n = B.length();
        int[][] lcs = new int[m+1][n+1];
        //lcs[i][j] indicates the lcs for A.substring(0, i) and B.substring(0,j);
        for (int i = 1; i <= m; i ++) {
            for (int j = 1; j <= n; j++) {
                if (A.charAt(i-1) == B.charAt(j-1)) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                } else {
                    lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
                }
            }
        }
        return lcs[m][n];
    }
}
```
