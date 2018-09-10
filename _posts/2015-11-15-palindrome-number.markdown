---
layout: post
title: 9 - Palindrome Number
date: 2015-11-15 17:33:12.000000000 -05:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
**Determine whether an integer is a palindrome. Do this without extra space.**

``` java
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int temp = x, rev = 0;
        while (temp != 0) {
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }
        return rev == x;
    }
}
```

``` python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None or x < 0:
            return False

        tmp, x_copy = 0, x
        while x_copy:
            tmp = tmp * 10 + x_copy % 10
            x_copy //= 10
        return tmp == x
```
