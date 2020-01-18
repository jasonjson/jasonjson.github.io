---
layout: post
title: 443 - String Compression
date: 2020-01-18
tags:
- Leetcode
categories:
- String
author: Jason
---
Given an array of characters, compress it in-place. The length after compression must always be smaller than or equal to the original array. Every element of the array should be a character (not int) of length 1. After you are done modifying the input array in-place, return the new length of the array.

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = start = 0
        while i < len(chars):
            while i < len(chars) and chars[i] == chars[start]:
                i += 1
            if i == start + 1:
                start = i
            else:
                nums = list(str(i - start))
                chars[start + 1: i] = nums
                start += len(nums) + 1
                i = start

        return len(chars)
```
