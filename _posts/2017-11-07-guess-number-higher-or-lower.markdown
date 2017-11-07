---
layout: post
title: 374 - Guess Number Higher Or Lower
date: 2017-11-07
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**We are playing the Guess Game. The game is as follows: I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I'll tell you whether the number is higher or lower. You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):**


```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
```
