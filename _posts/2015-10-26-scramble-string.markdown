---
layout: post
title: Scramble String
date: 2015-10-26 16:40:01.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
- Dynamic Programming
author: Jason
---
<p><strong><em>Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.</em></strong></p>


<p><a href="http://www.cnblogs.com/yuzhangcmu/p/4189152.html">See detailed explanations</a></p>
``` java
public class Solution {
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        
        int n = s1.length();
        boolean[][][] dp = new boolean[n][n][n + 1];
        //dp[i][j][k] denotes whether s1.substring(s1, s1+k) and s2.substring(s2, s2+k) is scramble string
        for (int k = 1; k <= n; k++) {
            for (int i = 0; i <= n - k; i++) {
                for (int j = 0; j <= n - k; j++) {
                    if (k == 1) {//compare len 1 string
                        dp[i][j][k] = s1.charAt(i) == s2.charAt(j);
                        continue;
                    }
                    for (int l = 1; l <= k; l++) {
                        boolean case1 = dp[i][j][l] && dp[i + l][j + l][k - l];
                        boolean case2 = dp[i][j + k - l][l] && dp[i + l][j][k - l];
                        if (case1 || case2) {
                            dp[i][j][k] = true;
                            break;
                        } 
                    }
                }
            }
        }
        return dp[0][0][n];
    }
}
```
``` java
public class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) return true;
        
        int[] letters = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            letters[s1.charAt(i) - 'a'] ++;
            letters[s2.charAt(i) - 'a'] --;
        }
        for (int n : letters) {
            if (n != 0) return false;
        }//相当于剪枝 去掉不可能
        
        for (int i = 1; i < s1.length(); i++) {
            if (isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) {
                return true;
            }
            if (isScramble(s1.substring(0, i), s2.substring(s1.length() - i)) && isScramble(s1.substring(i), s2.substring(0, s1.length() - i))) {
                return true;
            }
        }
        return false;
    }
}
```
