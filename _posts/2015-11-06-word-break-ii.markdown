---
layout: post
title: 140 - Word Break II
date: 2020-01-13
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

``` python
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        elif not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            elif len(word) == len(s):
                res.append(word)
            else:
                res.extend([word + ' ' + item for item in self.helper(s[len(word):], wordDict, memo)])
        memo[s] = res
        return res
```
