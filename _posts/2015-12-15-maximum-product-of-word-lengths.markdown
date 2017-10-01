---
layout: post
title: Maximum Product of Word Lengths
date: 2015-12-15 14:06:56.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- String
author: Jason
---
<p><strong><em>Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.</em></strong></p>


``` java
public class Solution {
    public int maxProduct(String[] words) {
        if (words == null || words.length == 0) return 0;
        
        int[] mask = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                mask[i] |= 1 << (words[i].charAt(j) - 'a');
            }
        }
        int result = 0;
        for (int i = 0; i < words.length; i ++) {
            for (int j = 1; j < words.length; j++) {
                if ((mask[i] & mask[j]) == 0) {
                    result = Math.max(result, words[i].length() * words[j].length());
                }
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public int maxProduct(String[] words) {
        if (words == null || words.length == 0) return 0;
        
        int result = 0;
        for (int i = 0; i < words.length; i++) {
            int[] letters = new int[26];
            for (char c : words[i].toCharArray()) {
                letters[c - 'a'] ++;
            }
            for (int j = i + 1; j < words.length; j++) {
                int k = 0;
                for (; k < words[j].length(); k++) {
                    if (letters[words[j].charAt(k) - 'a'] != 0) {
                        break;
                    }
                }
                if (k == words[j].length()) {
                    result = Math.max(result, words[i].length() * words[j].length());
                }
            }
        }
        return result;
    }
}
```
