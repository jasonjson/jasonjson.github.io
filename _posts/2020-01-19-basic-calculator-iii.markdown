---
layout: post
title: 772 - Basic Calculator III
date: 2020-01-19
tags:
- Leetcode
categories:
- Brain teaser
author: Jason
---
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

**Note**: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s += "$"
        return self.helper(s, 0)[0]
    def helper(self, s, index):
        stack = []
        num = 0
        sign = "+"
        while index < len(s):
            c = s[index]
            if c == " ":
                continue
                index += 1
            elif c.isdigit():
                num = num * 10 + int(c)
                index += 1
            elif c == "(":
                num, index = self.helper(s, index + 1)
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                elif sign == ")":
                    break
                sign = c
                num = 0
                index += 1
        return sum(stack), index
```
