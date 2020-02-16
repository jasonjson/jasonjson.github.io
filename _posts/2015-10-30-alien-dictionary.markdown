---
layout: post
title: 269 - Alien Dictionary
date: 2015-10-30 15:12:16.000000000 -04:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.**

``` python
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        char_dict = defaultdict(list)
        depth_dict = defaultdict(int)
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    char_dict[c1].append(c2)
                    depth_dict[c2] += 1
                    break

        chars = {c for word in words for c in word}
        queue = [c for c in chars if depth_dict[c] == 0]
        ret = []
        while queue:
            curr = queue.pop(0)
            ret.append(curr)
            for neighbor in char_dict[curr]:
                depth_dict[neighbor] -= 1
                if depth_dict[neighbor] == 0:
                    queue.append(neighbor)
        return "".join(ret) if len(ret) == len(chars) else ""
```
