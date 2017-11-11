---
layout: post
title: 392 - Is Subsequence
date: 2017-11-11
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string s and a string t, check if s is subsequence of t. You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).**


```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if not s:
            return True
        s_index = t_index = 0
        while t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                if s_index == len(s):
                    return True
            t_index += 1
        return False
```
