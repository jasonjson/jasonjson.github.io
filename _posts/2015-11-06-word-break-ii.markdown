---
layout: post
title: 140 - Word Break II
date: 2020-01-13
tags:
- Leetcode
categories:
- DFS
author: Jason
---
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

``` python
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def helper(string):
            if not string:
                return []
            ret = []
            for word in wordDict:
                if string.startswith(word):
                    if len(string) == len(word):
                        ret.append(word)
                    else:
                        ret.extend([word + " " + w for w in helper(string[len(word):])])
            return ret

        return helper(s)
```
