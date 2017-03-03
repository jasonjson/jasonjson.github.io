---
layout: post
title: Distinct Subsequences
date: 2015-10-21 12:49:08.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given a string S and a string T, count the number of distinct subsequences of T in S. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).</em></strong></p>


``` java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String S, String T) {
        int len1 = S.length(), len2 = T.length();
        int[][] count = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i++) {
            count[i][0] = 1;
        }
        for (int i = 1; i <= len1; i ++) {
            for (int j = 1; j <= len2; j++) {
                count[i][j] = count[i - 1][j];
                if (S.charAt(i - 1) == T.charAt(j - 1)) {
                    count[i][j] += count[i - 1][j - 1];
                }
            }
        }
        return count[len1][len2];
    }
}
```
