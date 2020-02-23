---
layout: post
title: 3 - Longest Substring Without Repeating Characters
date: 2015-10-21 14:28:39.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string, find the length of the longest substring without repeating characters.**

``` python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = defaultdict(int)
        start = ret = 0
        for i, c in enumerate(s):
            char_dict[c] += 1
            while char_dict[c] > 1:
                char_dict[s[start]] -= 1
                start += 1
            ret = max(ret, i - start + 1)
        return ret
```
