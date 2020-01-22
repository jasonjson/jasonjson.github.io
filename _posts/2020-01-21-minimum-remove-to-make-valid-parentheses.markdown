---
layout: post
title: 1249 - Minimum Remove To Make Valid Parentheses
date: 2020-01-21
tags:
- Leetcode
categories:
- String
author: Jason
---
Given a string s of '(' , ')' and lowercase English characters. Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string. Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as AB (A concatenated with B), where A and B are valid strings, or
* It can be written as (A), where A is a valid string.

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid_index = set()
        stack = []
        ret = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                valid_index.add(i)
                valid_index.add(stack[-1])
                stack.pop()

        for i, c in enumerate(s):
            if c in "()"and i in valid_index:
                ret.append(c)
            elif c.isalpha():
                ret.append(c)
        return "".join(ret)
```
