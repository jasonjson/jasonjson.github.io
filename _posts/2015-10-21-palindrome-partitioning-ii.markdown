---
layout: post
title: 132 - Palindrome Partitioning II
date: 2015-11-06 21:20:00.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.**


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

``` python
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        cut = [0] * (len(s) + 1)
        dp = self.is_pali(s)
        for i in xrange(len(s) + 1):
            cut[i] = i - 1
            for j in xrange(i):
                if dp[j + 1 - 1][i - 1]:
                    cut[i] = min(cut[i], cut[j] + 1)
        return cut[-1]

    def is_pali(self, s):
        dp = [[False] * len(s) for _ in xrange(len(s))]
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        return dp
```
