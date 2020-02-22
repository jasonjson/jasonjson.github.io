---
layout: post
title: 65 - Valid Number
date: 2015-10-26 17:19:21.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Validate if a given string is numeric.**

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        has_num = has_dot = has_exp = False
        for i, c in enumerate(s):
            if c.isdigit():
                has_num = True
            elif c == ".":
                if has_dot or has_exp:
                    return False
                has_dot = True
            elif c == "e":
                if has_exp or not has_num:
                    return False
                has_exp = True
                has_num = False
            elif c in "+-":
                if i > 0 and s[i - 1] != "e":
                    return False
            else:
                return False
        return has_num
```
