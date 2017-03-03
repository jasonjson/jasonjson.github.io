---
layout: post
title: Expression Evaluation
date: 2015-10-27 11:33:11.000000000 -04:00
tags: algorithm
categories:
- Brain teaser
- Integer
author: Jason
---
<p><strong><em>Given an expression string array, return the final result of this expression</em></strong></p>


``` java
public class Solution {
    /**
     * @param expression: an array of strings;
     * @return: an integer
     */
    public int evaluateExpression(String[] expression) {
        // write your code here
        if (expression == null || expression.length == 0) return 0;
        Stack<integer> num = new Stack<integer>();
        Stack<string> op = new Stack<string>();
        
        for (String s : expression) {
            if (isOp(s)) {
                if (s.equals("(")) {
                    op.push(s);
                } else if (s.equals(")")) {
                    while (!op.peek().equals("(")) {
                        num.push(eval(num.pop(), num.pop(), op.pop()));
                    }
                    op.pop();
                } else {
                    while (!op.isEmpty() && order(s) <= order(op.peek())) {
                        num.push(eval(num.pop(), num.pop(), op.pop()));
                    }
                    op.push(s);
                }
            } else {
                num.push(Integer.parseInt(s));
            }
        }
        while (!op.isEmpty()) {
            num.push(eval(num.pop(), num.pop(), op.pop()));
        }
        if (!num.isEmpty()) {
            return num.pop();
        } else {
            return 0;
        }
    }
    public int eval(int n1, int n2, String operator) {
        if (operator.equals("+")) {
            return n2 + n1;
        } else if (operator.equals("-")) {
            return n2 - n1;
        } else if (operator.equals("/")) {
            return n2 / n1;
        } else {
            return n2 * n1;
        }
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
};
```
