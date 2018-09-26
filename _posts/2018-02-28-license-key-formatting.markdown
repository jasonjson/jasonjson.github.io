---
layout: post
title: 482 - License Key Formatting
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes. Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase. Given a non-empty string S and a number K, format the string according to the rules described above.**

```python
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        if not S or not K:
            return ""

        new_s = "".join(S.split("-")).upper()
        ret = []
        index = len(new_s)
        while index > 0:
            left_index = index - K
            if left_index < 0:
                left_index = 0
            ret.append(new_s[left_index : index])
            index = left_index
        return "-".join(reversed(ret))
```
