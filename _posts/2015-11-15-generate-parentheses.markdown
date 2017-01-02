---
layout: post
title: Generate Parentheses
date: 2015-11-15 11:41:02.000000000 -05:00
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.</em></strong></p>

``` java
public class Solution {
    public List<string> generateParenthesis(int n) {
        List<string> result = new ArrayList<string>();
        helper(n, n, "", result);
        return result;
    }
    
    public void helper(int left, int right, String path, List<string> result) {
        if (left == 0 && right == 0) {
            result.add(path);
            return;
        }
        if (left > right || left < 0 || right < 0) {
            //when the number of "(" left to add is larger than the number of ")", stop
            return;
        }
        helper(left - 1, right, path + "(", result);
        helper(left, right - 1, path + ")", result);
    }
}
```
