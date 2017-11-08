---
layout: post
title: 383 - Ransom Note
date: 2017-11-07
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false. Each letter in the magazine string can only be used once in your ransom note.**


```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        random_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for char, cnt in random_counter.iteritems():
            if magazine_counter.get(char, 0) < cnt:
                return False

        return True
```
