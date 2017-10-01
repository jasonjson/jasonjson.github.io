---
layout: post
title: Palindrome Partitioning II
date: 2015-10-21 12:43:09.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given a string s, cut s into some substrings such that every substring is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.</em></strong></p>


``` java
public class Solution {
    /**
     * @param s a string
     * @return an integer
     */
    public int minCut(String s) {
        // write your code here
        if (s == null || s.length() == 0) return 0;
        
        int n = s.length();
        int[] cut = new int[n+1];
        for (int i = 0; i <= n; i++) {
            cut[i] = i - 1;
            //initialization: each char is different a b c d, for d, 
            //we have to cut three times
            //我们把cut[0]初始化为-1省去了边界条件的单独处理。否则"aa"报错
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (isPalin(s.substring(j,i))) {
                    cut[i] = Math.min(cut[i], cut[j] + 1);
                    //在j处cut
                }
            }
        }
        return cut[n];
    }
    
    public boolean isPalin(String s) {
        if (s == null || s.length() == 0) return false;
        
        int lo = 0, hi = s.length() - 1;
        while (lo <= hi) {
            if (s.charAt(lo) != s.charAt(hi)) {
                return false;
            }
            lo ++;
            hi --;
        }
        return true;
    }
};
```
``` java
public class Solution {
    /**
     * @param s a string
     * @return an integer
     */
    public int minCut(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int n = s.length();
        int[] cut = new int[n + 1];
        for (int i = 0; i <= n; i ++) {
            cut[i] = i - 1;
        }
        boolean[][] palin = isPalin(s);
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j ++) {
                if (palin[j][i-1]) {//i-1 not i, doesn't include ith char
                    cut[i] = Math.min(cut[i], cut[j] + 1);
                }
            }
        }
        return cut[n];
    }
    
    public boolean[][] isPalin(String s) {
        //if s.substring(i, j+1) is palindrome
        int n = s.length();
        boolean[][] palin = new boolean[n+1][n+1];
        for (int i = n - 1; i >= 0 ; i--) {//start from large index
            for (int j = i; j < n; j++) {
                if (j == i) {
                    palin[i][j] = true;
                } else if (j == i + 1) {
                    palin[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    palin[i][j] = (s.charAt(i) == s.charAt(j) && palin[i+1][j-1]);
                }
            }
        }
        return palin;
    }
};
```
