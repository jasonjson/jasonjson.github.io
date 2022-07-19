---
layout: post
title: 1047 - Remove All Adjacent Duplicates In String
date: 2022-07-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ret = []
        for c in s:
            if ret and ret[-1] == c:
                ret.pop()
            else:
                ret.append(c)
        return "".join(ret)
```
