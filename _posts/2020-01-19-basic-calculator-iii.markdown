---
layout: post
title: 772 - Basic Calculator III
date: 2020-01-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
Implement a basic calculator to evaluate a simple expression string. The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces. The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces. The integer division should truncate toward zero.

```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        s += "+"
        def helper(index):
            stack = []
            sign = "+"
            num = 0
            while index < len(s):
                c = s[index]
                if c == " ":
                    index += 1
                elif c.isdigit():
                    num = num * 10 + int(c)
                    index += 1
                elif c == "(":
                    num, index = helper(index + 1)
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
                    index += 1
                    num = 0
                    sign = c
            return sum(stack), index
        return helper(0)[0]
```
