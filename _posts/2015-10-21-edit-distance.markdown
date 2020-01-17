---
layout: post
title: 72 - Edit Distance
date: 2020-01-16
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.) You have the following 3 operations permitted on a word: Insert a character, Delete a character, Replace a character.


``` java
public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        int[][] dist = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i ++) {
            dist[i][0] = i;
        }
        for (int j = 0; j <= len2; j ++) {
            dist[0][j] = j;
        }
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dist[i][j] = dist[i-1][j-1];
                } else {
                    dist[i][j] = Math.min(dist[i-1][j-1], Math.min(dist[i-1][j], dist[i][j-1])) + 1;
                }
            }
        }
        return dist[len1][len2];
    }
}
```

``` python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
```
