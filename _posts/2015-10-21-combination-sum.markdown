---
layout: post
title: 39 - Combination Sum
date: 2015-10-21 03:41:33.000000000 -04:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.**

``` python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.helper(candidates, ret, [], target)
        return ret

    def helper(self, candidates, ret, curr, target):
        if target == 0:
            ret.append(curr[:])
            return
        for i, num in enumerate(candidates):
            if num <= target:
                self.helper(candidates[i:], ret, curr + [num], target - num)
```
