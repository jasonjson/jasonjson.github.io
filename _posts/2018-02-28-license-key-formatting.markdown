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
