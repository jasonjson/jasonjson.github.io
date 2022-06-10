---
layout: post
title: 150 - Evaluate Reverse Polish Notation
date: 2015-10-21 14:04:59.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+, -, *, /`. Each operand may be an integer or another expression.

**Note that division between two integers should truncate toward zero**.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

``` python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        for token in tokens:
            if token == "+":
                second, first = stack.pop(), stack.pop()
                stack.append(first + second)
            elif token == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif token == "*":
                second, first = stack.pop(), stack.pop()
                stack.append(first * second)
            elif token == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack.pop()
```
