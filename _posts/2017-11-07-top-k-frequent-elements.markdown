---
layout: post
title: 347 - Top K Frequent Elements
date: 2017-11-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a non-empty array of integers, return the k most frequent elements.**


```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return []
        counter = collections.Counter(nums)
        buckets = [[] for i in xrange(len(nums) + 1)]
        for num, cnt in counter.iteritems():
            buckets[cnt].append(num)
        ret = []
        for bucket in reversed(buckets):
            if len(ret) < k:
                ret.extend(bucket)
        return ret
```
