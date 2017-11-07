---
layout: post
title: 373 - Find K Pairs With Smallest Sums
date: 2017-11-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
**You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. Define a pair (u,v) which consists of one element from the first array and one element from the second array. Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.**


```python
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if not nums1 or not nums2:
            return []
        heap, ret = [], []
        for i in xrange(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and heap:
            k -= 1
            curr = heapq.heappop(heap)
            index1, index2 = curr[1], curr[2]
            ret.append([nums1[index1], nums2[index2]])
            if index2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))
        return ret
```
