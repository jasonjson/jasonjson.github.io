---
layout: post
title: 364 - Nested List Weight Sum II
date: 2020-01-16
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists. Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

```python
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        integer_list = self.helper(nestedList, 1)
        if not integer_list:
            return 0
        max_weight = max([k[1] for k in integer_list])
        return sum([k[0] * (max_weight - k[1] + 1) for k in integer_list])

    def helper(self, nestedList, weight):
        ret = []
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                ret.append([nestedInteger.getInteger(), weight])
            else:
                ret.extend(self.helper(nestedInteger.getList(), weight + 1))
        return ret
```
