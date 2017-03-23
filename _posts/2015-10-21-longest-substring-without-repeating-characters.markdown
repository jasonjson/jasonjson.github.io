---
layout: post
title: Longest Substring Without Repeating Characters
date: 2015-10-21 14:28:39.000000000 -04:00
tags:
- Algorithm
categories:
- String
author: Jason
---
<p><strong><em>Given a string, find the length of the longest substring without repeating characters.</em></strong></p>


``` java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int start = 0, maxLen = 0;
        int[] letters = new int[256];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            letters[c] ++;
            while (letters[c] > 1) {
                letters[s.charAt(start++)]--;
            }
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
}
```
``` java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int[] lastIndex = new int[256];
        Arrays.fill(lastIndex, -1);
        int start = 0, max = 1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (lastIndex[c] >= start) {
                start = lastIndex[c] + 1;
            }
            max = Math.max(max, i - start + 1);
            lastIndex[c] = i;
        }
        return max;
    }
}
```
