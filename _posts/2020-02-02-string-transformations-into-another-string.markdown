---
layout: post
title: 1153 - String Transformations Into Another String
date: 2020-02-02
tags:
- Leetcode
categories:
- String
author: Jason
---
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions. In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character. Return true if and only if you can transform str1 into str2.
[reference](https://leetcode.com/problems/string-transforms-into-another-string/discuss/355382/JavaC%2B%2BPython-Need-One-Unused-Character)

```python
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        convert_dict = {}
        for c1, c2 in zip(str1, str2):
            if convert_dict.setdefault(c1, c2) != c2:
                return False
        return len(set(str2)) < 26
```
