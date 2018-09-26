---
layout: post
title: 345 - Reverse Vowels Of A String
date: 2017-11-06
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Write a function that takes a string as input and reverse only the vowels of a string.**


```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowel = "aeiouAEIOU"
        s = list(s)
        lo, hi = 0, len(s) - 1
        while lo < hi: #not <= since lo, hi might move together
            if s[lo] in vowel and s[hi] in vowel:
                s[lo], s[hi] = s[hi], s[lo]
                lo += 1
                hi -= 1
            if s[lo] not in vowel:
                lo += 1
            if s[hi] not in vowel:
                hi -= 1
        return "".join(s)
```
