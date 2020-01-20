---
layout: post
title: 472 - Concatenated Words
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words. A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words:
            return []

        words_set = set(words)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words_set and suffix in words_set:
                    return True
                elif prefix in words_set and dfs(suffix):
                    return True
            return False

        return [w for w in words if dfs(w)]
```
