---
layout: post
title: 1181 - Before And After Puzzle
date: 2020-01-01
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a list of phrases, generate a list of Before and After puzzles. A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase. Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase. Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders. You should return a list of distinct strings sorted lexicographically.**

```python
from collections import defaultdict
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        if not phrases:
            return []

        first = defaultdict(list)
        last = defaultdict(list)
        for i, phrase in enumerate(phrases):
            words = phrase.split()
            first[words[0]].append(i)
            last[words[-1]].append(i)

        ret = set()
        for w in set(first) & set(last):
            for i in first[w]:
                for j in last[w]:
                    if i != j:
                        ret.add(phrases[j] + phrases[i].split(w, 1)[1])
        return sorted(list(ret))
```
