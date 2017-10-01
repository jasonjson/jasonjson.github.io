---
layout: post
title: Shortest Word Distance III
date: 2015-11-02 13:37:36.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.</p>

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.</p>
word1 and word2 may be the same and they represent two individual words in the list.</p>
You may assume word1 and word2 are both in the list.</em></strong></p>
``` java
public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int index1 = -1, index2 = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                index1 = i;
            }
            if (index1 != -1 && index2 != -1 && index1 != index2) {
                min = Math.min(min, Math.abs(index1 - index2));
            }//case["a","a"], word1 = "a", word2 ＝ "a" 更新index2前 算一次
            if (words[i].equals(word2)) {
                index2 = i;
            }
            if (index1 != -1 && index2 != -1 && index1 != index2) {
                min = Math.min(min, Math.abs(index1 - index2));
            }//更新后算一个
        }
        return min;
    }
}
```
