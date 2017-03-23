---
layout: post
title: N-Queens II
date: 2015-10-21 13:24:37.000000000 -04:00
tags:
- Algorithm
categories:
- DFS Backtracking
author: Jason
---
``` java
public class Solution {
    public int totalNQueens(int n) {
        if (n <= 0) return 0;
        
        int[] result = new int[1];
        helper(n, new ArrayList<integer>(), result);
        return result[0];
    }
    
    public void helper(int n, List<integer> cols, int[] result) {
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
    
    public boolean isValid(List<integer> cols, int col) {
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
