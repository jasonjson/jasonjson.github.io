---
layout: post
title: 680 - Valid Palindrome II
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                one = s[lo: hi]
                two = s[lo + 1: hi + 1]
                return one == one[::-1] or two == two[::-1]
            lo += 1
            hi -= 1
        return True
```
