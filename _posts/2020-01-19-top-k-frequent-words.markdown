---
layout: post
title: 692 - Top K Frequent Words
date: 2020-01-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a non-empty list of words, return the k most frequent elements. Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

```python
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return []

        buckets = [[] for _ in range(len(words))]
        for word, count in Counter(words).items():
            buckets[len(words) - count].append(word)

        for bucket in buckets:
            bucket.sort()

        return sum(buckets, [])[:k]
```
