---
layout: post
title: 127 - Word Ladder
date: 2015-10-21 12:57:57.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that: Only one letter can be changed at a time. Each intermediate word must exist in the dictionary.**

``` python
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "_" + word[i+1:]
                word_dict[new_word].append(word)

        queue = [(beginWord, 1)]
        seen = set()
        while queue:
            curr, step = queue.pop(0)
            seen.add(curr)
            if curr == endWord:
                return step
            for i in range(len(curr)):
                new_word = curr[:i] + "_" + curr[i+1:]
                for candidate in word_dict[new_word]:
                    if candidate not in seen:
                        queue.append((candidate, step + 1))
        return 0
```
