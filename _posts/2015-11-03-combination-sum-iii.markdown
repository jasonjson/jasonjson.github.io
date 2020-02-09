---
layout: post
title: 216 - Combination Sum III
date: 2015-11-03 17:04:46.000000000 -05:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.**


``` java
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (k <= 0 || n <= 0) return result;
        helper(1, k, n, new ArrayList<Integer>(), result);
        return result;
    }
    public void helper(int start, int k, int remain, List<Integer> path, List<List<Integer>> result) {
        if (k == 0) {
            if (remain == 0) {
                result.add(new ArrayList<Integer>(path));
            }
            return;
        }
        for (int i = start; i <= 9; i++) {
            if (i > remain) {
                return;
            }
            path.add(i);
            helper(i + 1, k - 1, remain - i, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

``` python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        ret = []
        self.helper(k, n, 1, [], ret)
        return ret

    def helper(self, k, n, start, curr, ret):
        if len(curr) == k:
            if n == 0:
                ret.append(curr[:])
            return
        for i in xrange(start, 10):
            if i <= n:
                self.helper(k, n - i, i + 1, curr + [i], ret)
```
