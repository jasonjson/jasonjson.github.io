---
layout: post
title: 350 - Intersection Of Two Arrays Ii
date: 2017-11-04
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Each element in the result should appear as many times as it shows in both arrays. The result can be in any order.**


```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        c1, c2 = Counter(nums1), Counter(nums2)
        ret = []
        for num in c1 & c2:
            ret.extend([num] * min(c1[num], c2[num]))
        return ret
```
