---
layout: post
title: 394 - Decode String
date: 2017-11-11
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given an encoded string, return it's decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.**


```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        stack = [["", 1]]
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append(["", num])
                num = 0
            elif char == "]":
                new_s, count = stack.pop()
                stack[-1][0] += new_s * count
            else:
                stack[-1][0] += char
        return stack.pop()[0]
```
