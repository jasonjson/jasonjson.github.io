---
layout: post
title: 227 - Basic Calculator II
date: 2020-01-09
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

**Note**: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

``` python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return -1
        s += "$"
        stack = []
        sign = "+"
        num = 0
        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)
```
