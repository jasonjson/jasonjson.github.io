---
layout: post
title: 1209 - Remove All Adjacent Duplicates In String Ii
date: 2022-07-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
You are given a string s and an integer k, a k **duplicate** removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k **duplicate** removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#", 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join([c * n for c, n in stack])
```
