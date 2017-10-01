---
layout: post
title: 52 - N-Queens II
date: 2015-10-21 13:24:37.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Follow up for N-Queens problem. Now, instead outputting board configurations, return the total number of distinct solutions.**

``` java
public class Solution {
    public int totalNQueens(int n) {
        if (n <= 0) return 0;

        int[] result = new int[1];
        helper(n, new ArrayList<Integer>(), result);
        return result[0];
    }

    public void helper(int n, List<Integer> cols, int[] result) {
        if (cols.size() == n) {
            result[0] ++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (isValid(cols, i)) {
                cols.add(i);
                helper(n, cols, result);
                cols.remove(cols.size() - 1);
            }
        }
    }

    public boolean isValid(List<Integer> cols, int col) {
        int row = cols.size();
        for (int i = 0; i < row; i++) {
            if (cols.get(i) == col || i + cols.get(i) == row + col || i - cols.get(i) == row - col) {
                return false;
            }
        }
        return true;
    }
}
```

``` python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [0]
        self.helper(n, [], ret)
        return ret[0]

    def helper(self, n, cols, ret):
        if (len(cols) == n):
            ret[0] += 1
            return
        for i in xrange(n):
            if self.is_valid(cols, i):
                cols.append(i)
                self.helper(n, cols, ret)
                cols.pop()

    def is_valid(self, cols, col):
        row = len(cols)
        for i in xrange(row):
            if col == cols[i] or abs(row - i) == abs(col - cols[i]):
                return False
        return True
```
