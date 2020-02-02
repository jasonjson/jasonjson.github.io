---
layout: post
title: 340 - Longest Substring with At Most K Distinct Characters
date: 2015-11-19 18:10:55.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a string s, find the length of the longest substring T that contains at most k distinct characters.**

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
