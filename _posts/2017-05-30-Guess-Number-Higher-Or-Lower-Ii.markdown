---
layout: post
title: 375 - Guess Number Higher Or Lower II
date: 2017-05-30
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**We are playing the Guess Game. The game is as follows: I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I'll tell you whether the number I picked is higher or lower. However, when you guess a particular number x,  and you guess wrong, you pay $x. You win the game when you guess the number I picked.**
[Explanation](https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/)


```python
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in xrange(n + 1)]
        #1 <= left <= n - 1, left + 1 <= right <= n
        for left in reversed(xrange(1, n)):
            for right in xrange(left + 1, n + 1):
                dp[left][right] = min(max(dp[left][i - 1], dp[i + 1][right]) + i for i in xrange(left, right))
        return dp[1][n]
```
