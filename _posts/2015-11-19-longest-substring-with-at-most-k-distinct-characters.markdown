---
layout: post
title: Longest Substring with At Most K Distinct Characters
date: 2015-11-19 18:10:55.000000000 -05:00
categories:
- Brain teaser
- Two Pointers
author: Jason
---
<p><strong><em>Given a string s, find the length of the longest substring T that contains at most k distinct characters.</em></strong></p>

``` java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        if (s == null || s.length() == 0) return 0;
        
        int start = 0, maxLen = 0, distinct = 0;
        int[] letter = new int[256];
        for (int i = 0; i < s.length(); i++) {
            letter[s.charAt(i)] ++;
            if (letter[s.charAt(i)] == 1) {
                distinct ++;
            }
            while (distinct > k) {
                if (--letter[s.charAt(start++)] == 0) {
                    distinct --;
                }
            }
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
}
```
