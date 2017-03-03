---
layout: post
title: Combination Sum III
date: 2015-11-03 17:04:46.000000000 -05:00
tags: algorithm
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.</em></strong></p>


``` java
public class Solution {
    public List<List<integer>> combinationSum3(int k, int n) {
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (k <= 0 || n <= 0) return result;
        helper(1, k, n, new ArrayList<integer>(), result);
        return result;
    }
    public void helper(int start, int k, int remain, List<integer> path, List<List<integer>> result) {
        if (k == 0) {
            if (remain == 0) {
                result.add(new ArrayList<integer>(path));
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
