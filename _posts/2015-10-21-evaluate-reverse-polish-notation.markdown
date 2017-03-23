---
layout: post
title: Evaluate Reverse Polish Notation
date: 2015-10-21 14:04:59.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression.</em></strong></p>


``` java
public class Solution {
    /**
     * @param tokens The Reverse Polish Notation
     * @return the value
     */
    public int evalRPN(String[] tokens) {
        // Write your code here
        if (tokens == null || tokens.length == 0) return 0;
        
        Stack<integer> stack = new Stack<integer>();
        //we avoid to check if tokens[i] is a number
        for (String s : tokens) {
            if (s.equals("+")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b + a); // bug b + a , not a + b
            } else if (s.equals("-")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b - a);
            } else if (s.equals("*")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b * a);
            } else if (s.equals("/")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b / a);  //bug b / a , not a / b
            } else {
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.peek();
    }
}
```
