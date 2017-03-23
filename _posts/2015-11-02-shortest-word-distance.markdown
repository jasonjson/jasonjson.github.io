---
layout: post
title: Shortest Word Distance
date: 2015-11-02 13:35:25.000000000 -05:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list. You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.</em></strong></p>


``` java
public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int index1 = -1, index2 = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                index1 = i;
            } else if (words[i].equals(word2)) {
                index2 = i;
            }
            if (index1 != -1 && index2 != -1) {
                min = Math.min(min, Math.abs(index1 - index2));
            }
        }
        return min;
    }
}
```
