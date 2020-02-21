---
layout: post
title: 953 - Verifying An Alien Dictionary
date: 2019-12-25
tags:
- Leetcode
categories:
- Array
author: Jason
---
**In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters. Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.**

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for w1, w2 in zip(words, words[1:]):
            i = j = 0
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    if order.index(w1[i]) > order.index(w2[j]):
                        return False
                    break
                i += 1
                j += 1
            if j == len(w2) and i < len(w1):
                return False
        return True
```
