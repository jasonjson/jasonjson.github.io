---
layout: post
title: Expression Add Operators
date: 2015-10-28 12:58:06.000000000 -04:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.**
[reference](http://segmentfault.com/a/1190000003797204")

``` java
public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<String>();
        if (num == null || num.length() == 0) return result;

        helper(num, target, 0, 0, "", result);
        return result;
    }

    public void helper(String num, int target, long prev, long currRes, String path, List<String> result) {
        if (num.length() == 0 && currRes == target) {
            result.add(new String(path));
            return;
        }
        for (int i = 1; i <= num.length(); i++) {
            String newStr = num.substring(0, i);
            if (newStr.charAt(0) == '0' && i > 1) return;//illegal numbers 01, 0123
            long newNum = Long.parseLong(newStr);//use long
            if (path.length() == 0) {//check if it's the first number
                helper(num.substring(i), target, newNum, newNum, path + newStr, result);
            } else {
                helper(num.substring(i), target, newNum, currRes + newNum, path + "+" + newStr, result);
                helper(num.substring(i), target, -newNum, currRes - newNum, path + "-" + newStr, result);
                helper(num.substring(i), target, prev * newNum, currRes - prev + prev * newNum, path + "*" + newStr, result);
            }
        }
    }
}
```
