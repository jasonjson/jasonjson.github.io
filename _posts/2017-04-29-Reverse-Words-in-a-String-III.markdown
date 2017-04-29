---
layout: post
title: Reverse Words in a String III
date: 2017-04-29
tags:
- Algorithm
categories:
- String
author: Jason
---
**Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.**

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #reverse a string: x[::-1]
        return " ".join(map(lambda x: x[::-1], s.split()))
```
