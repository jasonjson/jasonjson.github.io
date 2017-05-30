---
layout: post
title: Guess Number Higher Or Lower Ii
date: 2017-05-30
tags:
- Algorithm
categories:
- DP
author: Jason
---
**We are playing the Guess Game. The game is as follows: I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I'll tell you whether the number I picked is higher or lower. However, when you guess a particular number x,  and you guess wrong, you pay $x. You win the game when you guess the number I picked.**
[Explanation](https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/)

```python
#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii
#
# Example:
# 
# n = 10, I pick 8.
# 
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# 
# Game over. 8 is the number I picked.
# 
# You end up paying $5 + $7 + $9 = $21.
# 
# 
# 
# Given a particular n ≥ 1, find out how much money you need to have to
# guarantee a win.
#
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n + 1) for i in range(n + 1)]

        def helper(left, right):
            if left < right and dp[left][right] == 0:
                dp[left][right] = min(max(helper(left, pick - 1), helper(pick + 1, right)) + pick for pick in range(left, right))
            return dp[left][right]

        return helper(1, n)
```
