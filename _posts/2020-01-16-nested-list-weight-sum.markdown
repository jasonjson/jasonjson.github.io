---
layout: post
title: 339 - Nested List Weight Sum
date: 2020-01-16
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        num_weight_list = self.flatten(nestedList, 1)
        return sum([a[0] * a[1] for a in num_weight_list])

    def flatten(self, nestedList, weight):
        ret = []
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                ret.append([nestedInteger.getInteger(), weight])
            else:
                ret.extend(self.flatten(nestedInteger.getList(), weight + 1))
        return ret
```
