---
layout: post
title: 438 - Find All Anagrams In A String
date: 2020-01-19
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100. The order of output does not matter.

```python
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []

        counter_p = Counter(p)
        counter_s = Counter()
        start = found = 0
        ret = []
        for i, c in enumerate(s):
            counter_s[c] += 1
            if counter_s[c] == counter_p[c]:
                found += 1

            while found == len(counter_p):
                if i - start + 1 == len(p):
                    ret.append(start)
                counter_s[s[start]] -= 1
                if counter_s[s[start]] < counter_p[s[start]]:
                    found -= 1
                start += 1
        return ret
```
