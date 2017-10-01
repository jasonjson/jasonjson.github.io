---
layout: post
title: Keyboard Row
date: 2017-04-30
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.**

```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = list("qwertyuiop")
        line2 = list("asdfghjkl")
        line3 = list("zxcvbnm")
        ret = []
        for word in words:
            if self.contains(line1, word) or self.contains(line2, word) or self.contains(line3, word):
                ret.append(word)
        return ret

    def contains(self, line, word):
        for char in word.lower():
            if char not in line:
                return False
        return True
```
