---
layout: post
title: 150 -Evaluate Reverse Polish Notation
date: 2015-10-21 14:04:59.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression.**


``` java
public class Solution {
    /**
     * @param tokens The Reverse Polish Notation
     * @return the value
     */
    public int evalRPN(String[] tokens) {
        // Write your code here
        if (tokens == null || tokens.length == 0) return 0;

        Stack<Integer> stack = new Stack<Integer>();
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

``` python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        if not tokens:
            return -1

        number = []
        for token in tokens:
            try:
                number.append(int(token))
            except:
                num1 = number.pop()
                num2 = number.pop()
                number.append(self.cal(num2, num1, token))
        return number.pop()

    def cal(self, num2, num1, token):
        if token == "+":
            return num2 + num1
        elif token == "-":
            return num2 - num1
        elif token == "*":
            return num2 * num1
        elif token == "/":
            return int(float(num2) / num1)
```
