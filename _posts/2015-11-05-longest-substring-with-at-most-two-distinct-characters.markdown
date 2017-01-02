---
layout: post
title: Longest Substring with At Most Two Distinct Characters
date: 2015-11-05 16:22:23.000000000 -05:00
categories:
- Two Pointers
author: Jason
---
<p><strong><em>Given a string, find the length of the longest substring T that contains at most 2 distinct characters.</p>

For example, Given s = “eceba”,</p>
T is "ece" which its length is 3.</em></strong></p>
``` java
public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int max = 1, start = 0, distinct = 0;
        int[] counts = new int[256];
        for (int i = 0; i < s.length(); i++) {
            if (counts[s.charAt(i)] == 0) {
                distinct++;
            }
            counts[s.charAt(i)]++;
            while (distinct > 2) {
                counts[s.charAt(start)] --;
                if (counts[s.charAt(start)] == 0) {
                    distinct --;
                }
                start ++;
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }
}
```
