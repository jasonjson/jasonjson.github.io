---
layout: post
title: 320 - Generalized Abbreviation
date: 2015-12-22 16:04:37.000000000 -05:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Write a function to generate the generalized abbreviations of a word. Example: Given word = "word", return the following list (order does not matter): ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]**


``` python
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        ret = []
        self.helper(word, ret, "", False)
        return ret

    def helper(self, word, ret, curr, has_num):
        if not word:
            ret.append(curr)
            return
        self.helper(word[1:], ret, curr + word[0], False)
        if not has_num:
            for i in range(len(word)):
                num = i + 1
                self.helper(word[i+1:], ret, curr + str(num), True)
```
