---
layout: post
title: 1170 - Compare Strings By Frequency Of The Smallest Character
date: 2020-02-02
tags:
- Leetcode
categories:
- String
author: Jason
---
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2. Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

```python
from bisect import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        f_words = [w.count(min(w)) for w in words]
        f_words.sort()
        ret = []
        for query in queries:
            count = query.count(min(query))
            ret.append(len(f_words) - bisect(f_words, count))
        return ret
```
