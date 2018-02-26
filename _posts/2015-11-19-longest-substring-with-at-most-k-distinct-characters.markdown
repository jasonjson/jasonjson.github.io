---
layout: post
title: 340 - Longest Substring with At Most K Distinct Characters
date: 2015-11-19 18:10:55.000000000 -05:00
tags:
- Leetcode
categories:
- Two Pointers
author: Jason
---
**Given a string s, find the length of the longest substring T that contains at most k distinct characters.**


``` java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
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

``` python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if not s or not k:
            return 0

        ret = start = 0
        char_map = {}
        for i, char in enumerate(s):
            char_map[char] = char_map.get(char, 0) + 1
            while len(char_map) > k:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1
            ret = max(ret, i - start + 1)
        return ret
```
