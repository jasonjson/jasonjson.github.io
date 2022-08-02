---
layout: post
title: 890 - Find And Replace Pattern
date: 2022-08-02
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a list of `strings` words and a string `pattern`, return a list of `words[i]` that match `pattern`. You may return the answer in **any order**.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter `x` in the pattern with `p(x)`, we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

```python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    /*only need to care about the first index of each character*/
        def normalize(word):
            mapping = {}
            return [mapping.setdefault(c, len(mapping)) for c in word]

        normalized_pattern = normalize(pattern)
        return [w for w in words if normalize(w) == normalized_pattern]
```
