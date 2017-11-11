---
layout: post
title: 390 - Elimination Game
date: 2017-11-11
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list. Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers. We keep repeating the steps again, alternating left to right and right to left, until a single number remains. Find the last number that remains starting with a list of length n.**


```python
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        head = step = 1
        from_left = True
        remain = n
        while remain > 1:
            if from_left or remain % 2 == 1:
                head += step
            remain /= 2
            step *= 2
            from_left = not from_left
        return head
```
