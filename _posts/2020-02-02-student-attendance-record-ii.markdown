---
layout: post
title: 552 - Student Attendance Record Ii
date: 2020-02-02
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7. A student attendance record is a string that only contains the following three characters. A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

* 'A' : Absent.
* 'L' : Late.
* 'P' : Present.

```python
class Solution:
    def checkRecord(self, n: int) -> int:
        #dp[i] is the number of all possible attendance (without 'A')
        #ending with P, PL, PLL
        #dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        #the number of all possible attendance (with 'A') records
        #dp[i] *dp[n-1-i] i = 0,1,...,n-1
        if n == 0:
            return 0
        elif n == 1:
            return 3

        module = 10 ** 9 + 7
        dp = [1]
        for i in range(1, n + 1):
            dp.append(sum(dp[-3:]) % module)

        ret = sum(dp[-3:]) % module
        for i in range(n):
            ret += dp[i + 1] * dp[n - i]
            ret %= module

        return ret % (10**9 + 7)
```
