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
        index = [0]
        return self.helper(s, index)

    def helper(self, s, index):
        ret = []
        while (index[0] < len(s) and s[index[0]] != "]"):
            if s[index[0]].isdigit():
                num = 0
                while index[0] < len(s) and s[index[0]].isdigit():
                    num = num * 10 + int(s[index[0]])
                    index[0] += 1
                index[0] += 1
                string = self.helper(s, index)
                index[0] += 1
                ret.extend([string] * num)
            else:
                ret.append(s[index[0]])
                index[0] += 1
        return "".join(ret)
```
