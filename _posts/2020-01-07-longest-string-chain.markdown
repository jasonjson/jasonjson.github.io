---
layout: post
title: 1048 - Longest String Chain
date: 2020-01-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a list of words, each word consists of English lowercase letters. Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac". A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on. Return the longest possible length of a word chain with words chosen from the given list of words.**

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        words.sort(key=lambda x: len(x))
        word_count = {}
        for word in words:
            word_count[word] = 1
            for i in range(len(word)):
                pre_word = word[:i] + word[i+1:]
                if pre_word in word_count:
                    word_count[word] = word_count[pre_word] + 1
                    break
        return max(word_count.values())
```
