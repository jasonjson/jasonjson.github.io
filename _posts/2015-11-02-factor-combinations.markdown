---
layout: post
title: Factor Combinations
date: 2015-11-02 07:28:09.000000000 -05:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Numbers can be regarded as product of its factors. For example,</p>

8 = 2 x 2 x 2;</p>
  = 2 x 4.</p>
Write a function that takes an integer n and return all possible combinations of its factors.</em></strong></p>
``` java
public class Solution {
    public static List<List<Integer>> getFactors(int n) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (n <= 1) return result;

        helper(n, 2, new ArrayList<Integer>(), result);
        return result;
    }

    public static void helper(int remain, int start, List<Integer> path, List<List<Integer>> result) {
        if (remain == 1) {
            if (path.size() > 1) {//for 12, {12} can be in the result, we need to remove it
                result.add(new ArrayList<Integer>(path));
            }
            return;
        }
        for (int i = start; i <= remain; i++) {
            if (remain % i == 0) {
                path.add(i);
                helper(remain / i, i, path, result);{//first problem, i can be equal to n, for 37 we use path.size() > 1 to get the empty result, second problem, we use start to avoid duplicate results, like for 10, the result can be [2, 5] and [5, 2]
                path.remove(path.size() - 1);
            }
        }
    }
}
```
