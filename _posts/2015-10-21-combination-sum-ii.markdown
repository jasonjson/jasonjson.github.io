---
layout: post
title: 40 - Combination Sum II
date: 2015-10-21 03:41:59.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination.**


``` java
public class Solution {
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (num == null || num.length == 0) return result;

        Arrays.sort(num);
        helper(num, 0, target, new ArrayList<Integer>(), result);
        return result;
    }

    public void helper (int[] num, int start, int remain, List<Integer> list, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<Integer>(list));
            return;
        }
        for (int i = start; i < num.length; i++) {
            if (i > start && num[i] == num[i - 1]) continue;
            if (remain - num[i] >= 0) {
                list.add(num[i]);
                helper(num, i + 1, remain - num[i], list, result);
                list.remove(list.size() - 1);
            }
        }
    }
}
```

``` python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates:
            return []
        candidates.sort()
        ret = []
        self.helper(candidates, target, 0, [], ret)
        return ret

    def helper(self, candidates, remain, start, curr, ret):
        if remain == 0:
            ret.append(curr[:])
            return
        for i in xrange(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= remain:
                self.helper(candidates, remain - candidates[i], i + 1, curr + [candidates[i]], ret)
```
