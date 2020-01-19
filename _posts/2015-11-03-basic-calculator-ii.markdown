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
**Implement a basic calculator to evaluate a simple expression string.  The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero. You may assume that the given expression is always valid.**

``` python
class Solution:
    def calculate(self, s: str) -> int:
        s += "$"
        stack = []
        sign = "+"
        num = index = 0
        while index < len(s):
            c = s[index]
            if c == " ":
                index += 1
            elif c.isdigit():
                num = num * 10 + int(c)
                index += 1
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
                index += 1
        return sum(stack)
```
