---
layout: post
title: 263 - Ugly Number
date: 2015-10-21 02:41:36.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Write a program to check whether a given number is an ugly number. Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7. Note that 1 is typically treated as an ugly number.**


``` java
public class Solution {
    public boolean isUgly(int num) {
        if (num <= 0) return false;

        while (num % 5 == 0) {
            num = num / 5;
        }
        while (num % 3 == 0) {
            num = num / 3;
        }
        while (num % 2 == 0) {
            num = num / 2;
        }
        return num == 1;
    }
}
```

``` python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num % 5 == 0:
            num //= 5
        while num % 3 == 0:
            num //= 3
        while num % 2 == 0:
            num //= 2
        return num == 1
```
