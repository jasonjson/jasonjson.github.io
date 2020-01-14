---
layout: post
title: 616 - Add Bold Tag In String
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.**


```python
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:

        if not s:
            return ""

        is_bold = [False] * len(s)
        end = 0
        for i in xrange(len(s)):
            for word in dict:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            is_bold[i] = end > i

        ret = []
        i = 0
        while i < len(s):
            if not is_bold[i]:
                ret.append(s[i])
                i += 1
            else:
                j = i
                while j < len(s) and is_bold[j]:
                    j += 1
                ret.append("<b>" + s[i:j] + "</b>")
                i = j
        return "".join(ret)
```
