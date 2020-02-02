---
layout: post
title: 125 - Valid Palindrome
date: 2015-10-21 02:13:45.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.**

``` python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
```
