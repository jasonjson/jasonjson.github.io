---
layout: post
title: 507 - Perfect number
date: 2017-04-02
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself. Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.**


```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        total = 1
        for i in xrange(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                #如果num能被i整除，那num也能被商整除
                total += i + num / i

        return total == num
```
