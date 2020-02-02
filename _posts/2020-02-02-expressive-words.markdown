---
layout: post
title: 809 - Expressive Words
date: 2020-02-02
tags:
- Leetcode
categories:
- String
author: Jason
---
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo". For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

```python
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not words:
            return 0

        def helper(word):
            i = 0
            for j in range(len(S)):
                if i < len(word) and word[i] == S[j]:
                    i += 1
                elif S[j - 2:j + 1] != S[j] * 3 != S[j - 1: j + 2]:
                    return False
            return i == len(word)

        return sum(helper(w) for w in words)
```
