---
layout: post
title: Evaluate Reverse Polish Notation
date: 2015-11-06 11:43:57.000000000 -05:00
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Evaluate the value of an arithmetic expression in Reverse Polish Notation.<br />

Valid operators are +, -, *, /. Each operand may be an integer or another expression.</em></strong></p>
``` java
public class Solution {
    public int evalRPN(String[] tokens) {
        if (tokens == null || tokens.length == 0) return 0;
        Stack<integer> stack = new Stack<integer>();
        for (String s : tokens) {
            if (isOp(s)) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                if (s.equals("+")) {
                    stack.push(num2 + num1);
                } else if (s.equals("-")) {
                    stack.push(num2 - num1);
                } else if (s.equals("*")) {
                    stack.push(num2 * num1);
                } else if (s.equals("/")) {
                    stack.push(num2 / num1);
                }
            } else {
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.pop();
    }
    
    public boolean isOp(String s) {
        if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")) {
            return true;
        } else {
            return false;
        }
    }
}
```
