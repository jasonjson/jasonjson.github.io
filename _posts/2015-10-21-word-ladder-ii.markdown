---
layout: post
title: 126 - Word Ladder II
date: 2015-10-21 12:58:31.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end.**

``` python
from typing import List
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList:
            return []

        word_map = self.construct(wordList)
        visited = {beginWord}
        ret = []
        step = self.find_step(beginWord, endWord, word_map)
        self.helper(visited, endWord, word_map, [beginWord], ret, step)
        return ret

    def find_step(self, beginWord, endWord, word_map):
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            curr, step = queue.pop(0)
            if curr == endWord:
                return step
            visited.add(curr)
            step += 1
            for i in range(len(curr)):
                new_curr = curr[:i] + "_" + curr[i+1:]
                for candidate in word_map[new_curr]:
                    if candidate not in visited:
                        queue.append((candidate, step))
        return 0

    def helper(self, visited, endWord, word_map, path, ret, step):
        if len(path) > step:
            return
        elif path[-1] == endWord:
            ret.append(path[:])
            return
        prev = path[-1]
        for i in range(len(prev)):
            new_word = prev[:i] + "_" + prev[i+1:]
            for candidate in word_map[new_word]:
                if candidate not in visited:
                    path.append(candidate)
                    visited.add(candidate)
                    self.helper(visited, endWord, word_map, path, ret, step)
                    visited.remove(candidate)
                    path.pop()

    def construct(self, wordList):
        word_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "_" + word[i+1:]
                word_map[new_word].append(word)
        return word_map
```
