---
layout: post
title: 347 - Top K Frequent Elements
date: 2019-12-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a non-empty array of integers, return the k most frequent elements.**

```python
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []

        buckets = [[] for _ in range(len(nums))]
        for num, count in Counter(nums).items():
            buckets[len(nums) - count].append(num)
        return sum(buckets, [])[:k]
```
