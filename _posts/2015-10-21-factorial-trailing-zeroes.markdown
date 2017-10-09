---
layout: post
title: 172 - Factorial Trailing Zeroes
date: 2015-10-21 02:36:12.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an integer n, return the number of trailing zeroes in n!. Note: Your solution should be in logarithmic time complexity.**


``` java
public class Solution {
//to compute the number of trailing zeros, we need to first think clear about what will generate a trailing 0? Obviously, a number multiplied by 10 will have a trailing 0 added to it. So we only need to find out how many 10's will appear in the expression of the factorial. Since 10 = 2 * 5 and there are a bunch more 2's (each even number will contribute at least one 2), we only need to count the number of 5's.
    public int trailingZeroes(int n) {
        int count = 0;
        if (n < 0) return -1;
        while (n > 0) {
            count += n / 5;
            n = n / 5;
        }
        return count;
    }
    //recursive
    public int trailingZeroes(int n) {
        if (n < 0) return -1;
        if (n == 0) return 0;
        return n / 5 + trailingZeroes(n / 5);
    }
}
```

``` python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        ret = 0
        while n:
            ret += n / 5
            n /= 5
        return ret
```
