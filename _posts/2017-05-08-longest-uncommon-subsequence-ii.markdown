---
layout: post
title: Longest Uncommon Subsequence ii
date: 2017-05-08
tags:
- Algorithm
categories:
- String
author: Jason
---
**Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings. A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string. The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.**

```python
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not self.is_subseq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1

    def is_subseq(self, word1, word2):
        i = 0
        for char in word2:
            if i < len(word1) and word1[i] == char:
                i += 1
        return i == len(word1)
```
