---
layout: post
title: 336 - Palindrome Pairs
date: 2019-12-26
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.**

```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []

        def is_pali(word):
            return word == word[::-1]

        word_index = {word: i for i, word in enumerate(words)}
        ret = []

        for word, index in word_index.items():
            for j in range(len(word) + 1):
                # when j = 0 or len(word), whole string is checked
                pref = word[:j]
                suff = word[j:]
                if is_pali(pref):
                    one = suff[::-1]
                    if one != word and one in word_index:
                        ret.append([word_index[one], index])
                if j != len(word) and is_pali(suff):
                    one = pref[::-1]
                    if one != word and one in word_index:
                        ret.append([index, word_index[one]])
        return ret
```
