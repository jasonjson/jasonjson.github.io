---
layout: post
title: Edit Distance
date: 2015-10-21 12:45:39.000000000 -04:00
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.) You have the following 3 operations permitted on a word: Insert a character, Delete a character, Replace a character</em></strong></p>

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
