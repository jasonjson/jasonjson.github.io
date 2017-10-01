---
layout: post
title: Palindrome Partitioning II
date: 2015-11-06 21:20:00.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
- Palindrome
author: Jason
---
<p><strong><em>Given a string s, partition s such that every substring of the partition is a palindrome.</p>

Return the minimum cuts needed for a palindrome partitioning of s.</em></strong></p>
``` java
public class Solution {
    public int minCut(String s) {
        if (s == null || s.length() == 0) return 0;

        boolean[][] isPalin = helper(s);
        int[] cut = new int[s.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
            cut[i] = i - 1;//初始化的目的是设置一个higher bound,注意cut[0]=-1
            for (int j = 0; j < i; j++) {//j不能等于i
                if (isPalin[j][i-1]) {
                    cut[i] = Math.min(cut[i], cut[j] + 1);
                }
            }
        }
        return cut[s.length()];
    }

    public boolean[][] helper(String s) {
        int n = s.length();
        boolean[][] isPalin = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
        //因为我们需要isPalin[i+1][j-1],所以i从n-1开始, j从i开始
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && ((j - i <= 2) || isPalin[i+1][j-1])) {
                    isPalin[i][j] = true;
                //j - i <= 2 deal with case "aa", length 1 or 2 string
                }
            }
        }
        return isPalin;
    }
}
```
