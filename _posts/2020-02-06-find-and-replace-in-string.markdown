---
layout: post
title: 833 - Find And Replace In String
date: 2020-02-06
tags:
- Leetcode
categories:
- String
author: Jason
---
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size). Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

```python
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:

        ret = list(S)
        for i, x, y in zip(indexes, sources, targets):
            if S[i: i + len(x)] == x:
                ret[i] = y
                for j in range(i + 1, i + len(x)):
                    ret[j] = ""
        return "".join(ret)
```
