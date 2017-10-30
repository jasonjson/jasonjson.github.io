---
layout: post
title: 318 - Maximum Product of Word Lengths
date: 2015-12-15 14:06:56.000000000 -05:00
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.**


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

``` python
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        ord_map = {}
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - ord("a")))
            ord_map[mask] = max(ord_map.get(mask, 0), len(word))
        return max([ord_map[x] * ord_map[y] for x in ord_map for y in ord_map if not x & y] or [0])
```
