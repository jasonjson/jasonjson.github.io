---
layout: post
title: 159 - Longest Substring with At Most Two Distinct Characters
date: 2015-11-05 16:22:23.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

``` python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0

        ret = start = 0
        char_map = defaultdict(int)
        for i, c in enumerate(s):
            char_map[c] += 1
            while len(char_map) > 2:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1
            ret = max(ret, i - start + 1)
        return ret
```
