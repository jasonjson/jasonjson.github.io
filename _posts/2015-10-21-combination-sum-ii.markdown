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
    public List<List<integer>> combinationSum2(int[] num, int target) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (num == null || num.length == 0) return result;

        Arrays.sort(num);
        helper(num, 0, target, new ArrayList<integer>(), result);
        return result;
    }

    public void helper (int[] num, int start, int remain, List<integer> list, List<List<integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<integer>(list));
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
        self.helper(candidates, 0, [], ret, target)
        return ret

    def helper(self, candidates, start, curr, ret, remain):
        if remain == 0:
            ret.append(copy.deepcopy(curr))
            return
        for i in xrange(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= remain:
                curr.append(candidates[i])
                self.helper(candidates, i + 1, curr, ret, remain - candidates[i])
                curr.pop()
```
