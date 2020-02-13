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
from heapq import heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return []

        ret = []
        pq = [[-v, k] for k, v in Counter(words).items()]
        heapify(pq)
        while len(ret) < k:
            ret.append(heappop(pq)[1])
        return ret
```
