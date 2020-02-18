---
layout: post
title: 126 - Word Ladder II
date: 2015-10-21 12:58:31.000000000 -04:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end.**

``` python
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        prev[beginWord] = [[beginWord]]
        while prev:
            curr = defaultdict(list)
            for word in prev:
                if word == endWord:
                    return prev[word]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(word)):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            curr[new_word].extend(w + [new_word] for w in prev[word])
            word_set -= set(curr)
            prev = curr
        return []
```
