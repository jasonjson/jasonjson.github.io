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
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if order.index(w1[i]) > order.index(w2[i]):
                        return False
                    break
                if i == len(w2) - 1 and i < len(w1) - 1:
                    return False

        return True
```
