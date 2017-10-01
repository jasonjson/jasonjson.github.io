---
layout: post
title: Different Ways to Add Parentheses
date: 2015-11-02 16:24:34.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.</em></strong></p>


``` java
public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        if (input == null || input.length() == 0) return new ArrayList<Integer>();
        
        List<String> path = new ArrayList<String>();
        for (int i = 0; i < input.length(); i++) {
            int j = i;
            while (j < input.length() && Character.isDigit(input.charAt(j))) {
                j++;//string has no such isDigit method
            }
            path.add(input.substring(i,j));
            if (j < input.length()) {
                path.add(input.substring(j, j + 1));
            }//i will increment in for loop, so no need to increment j here
            i = j;
        }//separate strings into numbers and operators
        return helper(path, 0, path.size() - 1);
    }
    
    public List<Integer> helper(List<String> path, int lo, int hi) {
        List<Integer> result = new ArrayList<Integer>();
        if (lo == hi) {
            result.add(Integer.parseInt(path.get(lo)));//!!transfer to int
            return result;
        }
        for (int i = lo + 1; i <= hi - 1; i+=2) {
            String operator = path.get(i);
            List<Integer> left = helper(path, lo, i - 1);//this is like unique binary search trees
            List<Integer> right = helper(path, i + 1, hi);
            for (int m : left) {
                for (int n : right) {
                    if (operator.equals("+")) {
                        result.add(m + n);
                    } else if (operator.equals("-")) {
                        result.add(m - n);
                    } else {
                        result.add(m * n);
                    }
                }
            }
        }
        return result;
    }
}
```
