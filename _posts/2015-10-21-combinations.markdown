---
layout: post
title: Combinations
date: 2015-10-21 03:41:06.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.**


``` java
public class Solution {
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    public List<List<integer>> combine(int n, int k) {
        // write your code here
        List<List<integer>> result = new ArrayList<List<integer>>();
        if (n == 0 || k == 0) return result;
        List<integer> list = new ArrayList<integer>();

        combineUtil(n, k, 1, list, result);
        return result;
    }

    public void combineUtil(int n, int k, int start, List<integer> list, List<List<integer>> result) {
        if (list.size() == k) {
            result.add(new ArrayList<integer>(list));
            return; // for subset don't return
            //for permutation or a fixed size list, return so save time.
        }

        for (int i = start; i <= n; i++) {
            list.add(i);
            combineUtil(n, k, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

``` python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        if not k or not n:
            return []

        ret = []
        self.helper(1, n, k, [], ret)
        return ret

    def helper(self, start, n, k, curr, ret):
        if len(curr) == k:
            ret.append(curr[:])
            return
        for i in xrange(start, n + 1):
            curr.append(i)
            self.helper(i + 1, n, k, curr, ret)
            curr.pop()
```
