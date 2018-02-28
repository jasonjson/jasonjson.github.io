---
layout: post
title: 734 - Sentence Similarity
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar. Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.**


```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(words1) != len(words2):
            return False
        word_map = collections.defaultdict(set)
        for (a, b) in pairs:
            word_map[a].add(b)
            word_map[b].add(a)

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w2 not in word_map[w1]:
                return False
        return True
```
