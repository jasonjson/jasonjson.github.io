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
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S or not K:
            return ""

        S = S.replace("-", "").upper()
        end = len(S)
        ret = []
        while end > 0:
            start = end - K
            if start < 0:
                start = 0
            ret.append(S[start: end])
            end = start
        return "-".join(reversed(ret))
```
