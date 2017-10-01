---
layout: post
title: Convert Expression to Polish Notation
date: 2015-10-21 14:13:38.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given an expression string array, return the Polish notation of this expression. (remove the parentheses)</em></strong></p>


``` java
public class Solution {
    public ArrayList<string> convertToPN(String[] expression) {
        ArrayList<string> result = new ArrayList<string>();
        if (expression == null || expression.length == 0) return result;
        Stack<string> stack = new Stack<string>();
        for (int i = expression.length - 1; i >= 0; i--) {
            String s = expression[i];
            if (isOp(s)) {
                if (s.equals(")")) {
                    stack.push(s);
                } else if (s.equals("(")) {
                    while (!stack.isEmpty() && !stack.peek().equals(")") {
                        result.add(stack.pop());
                    }
                    stack.pop();
                } else {
                    while (!stack.isEmpty() && order(s) < order(stack.peek())) {
                        result.add(stack.pop());
                    }
                    stack.push(s);
                }
            } else {
                result.add(s);
            }
        }
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        Collections.reverse(result);
        return result;
    }
    public boolean isOp(String s) {
        if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/") || s.equals("(") || s.equals(")")) {
            return true;
        } else {
            return false;
        }
    }
    public int order(String s) {
        if (s.equals("*") || s.equals("/")) {
            return 2;
        } else if (s.equals("+") || s.equals("-")) {
            return 1;
        } else {
            return 0;
        }
    }
}
```
