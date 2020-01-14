---
layout: post
title: 737 - Sentence Similarity II
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.**


```python
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        if len(words1) != len(words2):
            return False

        word_map = collections.defaultdict(set)
        for a, b in pairs:
            word_map[a].add(b)
            word_map[b].add(a)

        for w1, w2 in zip(words1, words2):
            visited = set([w1])
            if not self.verify(w1, w2, word_map, visited):
                return False
        return True


    def verify(self, w1, w2, w_map, visited):
        if w1 == w2:
            return True
        for word in w_map[w1]:
            if word not in visited:
                visited.add(word)
                if self.verify(word, w2, w_map, visited):
                    return True
                visited.discard(word)
        return False
```

``` python
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False
        union = {}
        for (a, b) in pairs:
            p1, p2 = self.find(a, union), self.find(b, union)
            union[p1] = p2

        for w1, w2 in zip(words1, words2):
            if self.find(w1, union) != self.find(w2, union):
                return False
        return True


    def find(self, s, union):
        if s == union.get(s, s):
            union[s] = s
            return s
        else:
            return self.find(union[s], union)

```
