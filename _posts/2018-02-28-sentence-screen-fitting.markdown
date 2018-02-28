---
layout: post
title: 418 - Sentence Screen Fitting
date: 2018-02-28
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.**


```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_s = " ".join(sentence) + " "
        start = 0
        for i in xrange(rows):
            start += cols
            if new_s[start % len(new_s)] == " ":
                start += 1
            else:
                while start > 0 and new_s[(start - 1) % len(new_s)] != " ":
                    start -= 1
        return start / len(new_s)
```
