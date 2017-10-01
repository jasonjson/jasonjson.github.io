---
layout: post
title: 39 - Combination Sum
date: 2015-10-21 03:41:33.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.**


``` java
public class Solution {
    public List<List<integer>> combinationSum(int[] candidates, int target) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (candidates == null || candidates.length == 0) return result;
        List<integer> list = new ArrayList<integer>();

        Arrays.sort(candidates);
        helper(candidates, 0, target, list, result);
        return result;
    }

    public void helper(int[] candidates, int start, int gap, List<integer> list, List<List<integer>> result) {
        if (gap == 0) {
            result.add(new ArrayList<integer>(list));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidate[i] == candidates[i - 1]) continue;
            if (gap - candidates[i] >= 0) {
                list.add(candidates[i]);
                helper(candidates, i, gap - candidates[i], list, result);
                list.remove(list.size() - 1);
            }
        }
    }
}
```

``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        candidates.sort()
        ret = []
        self.helper(candidates, 0, [], ret, target)
        return ret

    def helper(self, candidates, index, curr, ret, remain):
        if remain == 0 :
            ret.append(copy.deepcopy(curr))
            return
        for i in xrange(index, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            elif candidates[i] <= remain:
                curr.append(candidates[i])
                self.helper(candidates, i, curr, ret, remain - candidates[i])
                curr.pop()
```
